from module import RNN
from torch import nn
from transformers import BertModel
from utils import seq_len_to_mask

from . import BasicModule


class LM(BasicModule):
    def __init__(self, cfg):
        super(LM, self).__init__()
        self.bert = BertModel.from_pretrained(cfg.lm_file, num_hidden_layers=cfg.num_hidden_layers)
        self.bilstm = RNN(cfg)
        self.fc = nn.Linear(cfg.hidden_size, cfg.num_relations)
        self.dropout = nn.Dropout(cfg.dropout)

    def forward(self, x):
        word, lens = x['word'], x['lens']
        mask = seq_len_to_mask(lens, mask_pos_to_true=False)
        last_hidden_state, pooler_output = self.bert(word, attention_mask=mask)
        out, out_pool = self.bilstm(last_hidden_state, lens)
        out_pool = self.dropout(out_pool)
        output = self.fc(out_pool)

        return output
