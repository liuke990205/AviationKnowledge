# coding=utf-8

# from extraction import _rel_extraction
import csv
import logging

import hydra
# noinspection PyUnresolvedReferences
import models
import torch
from hydra import utils
from preprocess import _serialize_sentence, _convert_tokens_into_index, _add_pos_seq, _handle_relation_data
from serializer import Serializer
from utils import load_pkl, load_csv

logger = logging.getLogger(__name__)


def _preprocess_data(data, cfg):
    vocab = load_pkl('C:/Users/26407/Desktop/HelloWorld/hello/toolkit/deepke/data/out/vocab.pkl', verbose=False)
    relation_data = load_csv('C:/Users/26407/Desktop/HelloWorld/hello/toolkit/deepke/data/origin/relation.csv',
                             verbose=False)
    rels = _handle_relation_data(relation_data)
    cfg.vocab_size = vocab.count
    serializer = Serializer(do_chinese_split=cfg.chinese_split)
    serial = serializer.serialize

    _serialize_sentence(data, serial, cfg)
    _convert_tokens_into_index(data, vocab)
    _add_pos_seq(data, cfg)
    # logger.info('start sentence preprocess...')
    formats = '\nsentence: {}\nchinese_split: {}\nreplace_entity_with_type:  {}\nreplace_entity_with_scope: {}\n' \
              'tokens:    {}\ntoken2idx: {}\nlength:    {}\nhead_idx:  {}\ntail_idx:  {}'
    # logger.info(
    #     formats.format(data[0]['sentence'], cfg.chinese_split, cfg.replace_entity_with_type,
    #                    cfg.replace_entity_with_scope, data[0]['tokens'], data[0]['token2idx'], data[0]['seq_len'],
    #                    data[0]['head_idx'], data[0]['tail_idx']))
    return data, rels


def _get_predict_instance(cfg, relationlist):
    # flag = input('是否使用范例[y/n]，退出请输入: exit .... ')
    # flag = flag.strip().lower()
    # if flag == 'y' or flag == 'yes':
    #    sentence = '《乡村爱情》是由知名导演赵本山在1985年所拍摄的农村青春偶像剧。'
    #    head = '乡村爱情'
    #    tail = '赵本山'
    #    head_type = '影视作品'
    #    tail_type = '人物'
    # elif flag == 'n' or flag == 'no':

    # sentence = input('请输入句子：')
    # head = input('请输入句中需要预测关系的头实体：')
    # head_type = input('请输入头实体类型（可以为空，按enter跳过）：')
    # tail = input('请输入句中需要预测关系的尾实体：')
    # tail_type = input('请输入尾实体类型（可以为空，按enter跳过）：')

    sentence = relationlist[0]
    head = relationlist[1]
    head_type = relationlist[2]
    tail = relationlist[3]
    tail_type = relationlist[4]
    # elif flag == 'exit':
    # sys.exit(0)
    # else:
    # print('please input yes or no, or exit!')
    # _get_predict_instance()

    instance = dict()
    instance['sentence'] = sentence.strip()
    instance['head'] = head.strip()
    instance['tail'] = tail.strip()
    if head_type.strip() == '' or tail_type.strip() == '':
        cfg.replace_entity_with_type = False
        instance['head_type'] = 'None'
        instance['tail_type'] = 'None'
    else:
        instance['head_type'] = head_type.strip()
        instance['tail_type'] = tail_type.strip()

    return instance


# 自定义模型存储的路径
fp = 'C:/Users/26407/Desktop/HelloWorld/hello/toolkit/deepke/checkpoints/2020-07-09_20-39-47/cnn_epoch50.pth'
temp_file_dir = "C:/Users/26407/Desktop/HelloWorld/hello/toolkit/rel_data.csv"


@hydra.main(config_path='conf/config.yaml')
def main(cfg):
    cwd = utils.get_original_cwd()
    cfg.cwd = cwd
    cfg.pos_size = 2 * cfg.pos_limit + 2
    # print(cfg.pretty())

    # relationlist = []
    relType = []

    textfile = open(temp_file_dir, 'r')
    writetextfile = open(temp_file_dir, 'a')
    reader = csv.reader(textfile)
    new_rel = []
    for rel in reader:

        # for rel in relationlist:
        # get predict instance

        instance = _get_predict_instance(cfg, rel)
        # print(instance)
        data = [instance]
        data, rels = _preprocess_data(data, cfg)

        # preprocess data

        # model
        __Model__ = {
            'cnn': models.PCNN,
            'rnn': models.BiLSTM,
            'transformer': models.Transformer,
            'gcn': models.GCN,
            'capsule': models.Capsule,
            'lm': models.LM,
        }

        # 最好在 cpu 上预测
        # cfg.use_gpu = False
        if cfg.use_gpu and torch.cuda.is_available():
            device = torch.device('cuda', cfg.gpu_id)
        else:
            device = torch.device('cpu')
        # logger.info(f'device: {device}')

        model = __Model__[cfg.model_name](cfg)

        # logger.info(f'model name: {cfg.model_name}')
        # logger.info(f'\n {model}')
        model.load(fp, device=device)
        model.to(device)
        model.eval()

        x = dict()
        x['word'], x['lens'] = torch.tensor([data[0]['token2idx']]), torch.tensor([data[0]['seq_len']])
        if cfg.model_name != 'lm':
            x['head_pos'], x['tail_pos'] = torch.tensor([data[0]['head_pos']]), torch.tensor([data[0]['tail_pos']])
            if cfg.model_name == 'cnn':
                if cfg.use_pcnn:
                    x['pcnn_mask'] = torch.tensor([data[0]['entities_pos']])

        for key in x.keys():
            x[key] = x[key].to(device)

        with torch.no_grad():
            y_pred = model(x)
            y_pred = torch.softmax(y_pred, dim=-1)[0]
            prob = y_pred.max().item()
            prob_rel = list(rels.keys())[y_pred.argmax().item()]
            # print(prob_rel)
            # logger.info(f"\"{data[0]['head']}\" 和 \"{data[0]['tail']}\" 在句中关系为：\"{prob_rel}\"，置信度为{prob:.2f}。")
            rel.append(prob_rel)
        new_rel.append(rel)
    print(new_rel)
    writer = csv.writer(writetextfile)
    for new in new_rel:
        writer.writerow(new)

    # os.remove("/Users/anyuanming/Desktop/testfile1.csv")

    # if cfg.predict_plot:
    #     # maplot 默认显示不支持中文
    #     plt.rcParams["font.family"] = 'Arial Unicode MS'
    #     x = list(rels.keys())
    #     height = list(y_pred.cpu().numpy())
    #     plt.bar(x, height)
    #     for x, y in zip(x, height):
    #         plt.text(x, y, '%.2f' % y, ha="center", va="bottom")
    #     plt.xlabel('关系')
    #     plt.ylabel('置信度')
    #     plt.xticks(rotation=315)
    #     plt.show()


if __name__ == '__main__':
    main()
