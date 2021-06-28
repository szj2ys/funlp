# *_*coding:utf-8 *_*
"""
Descri：
"""
from os.path import dirname, abspath, join


class dirs(dict):
    # 获取项目根目录
    ROOT = dirname(abspath(__file__))

    # 数据文件存放路径
    DATASETS_DIR = join(ROOT, "datasets")

    # 图片文件路径
    IMAGES_DIR = join(DATASETS_DIR, "images")

    # 字体文件路径
    FONTS_DIR = join(DATASETS_DIR, "fonts")

    # 结果文件路径
    RESULTS_DIR = join(DATASETS_DIR, "results")

    # log文件路径
    LOGS_DIR = join(DATASETS_DIR, "logs")

    BEAUTILS_DIR = join(ROOT, "beautils")


## 如果datasets目录不存在，则自动创建
# if not os.path.exists(DIR_DATASETS):
#     Path(DIR_DATASETS).mkdir(exist_ok=True)


class files:
    ENVJSON = join(dirs.BEAUTILS_DIR, "env.json")
    # 错误日志文件
    LOGS_ERRORS = join(dirs.LOGS_DIR, "errors.log")

    # 日志文件
    LOGS = join(dirs.LOGS_DIR, "everythings.log")

    # 停用词路径
    STOPWORDS = join(dirs.DATASETS_DIR, "stopwords.txt")
    # print(FILE_STOP_WORDS)
    # 自定义切词表
    USER_DICT = join(dirs.DATASETS_DIR, "userdict.txt")

    # 原始新闻语料
    RAW_NEWS = join(dirs.DATASETS_DIR, "data.csv")

    # 程度副词文件
    ADVERB = join(dirs.DATASETS_DIR, "sentifiles", "desc_words.txt")

    # so_pmi训练得到的情感词文件
    SENTI_WORDS = join(dirs.DATASETS_DIR, "sentifiles", "senti.txt")
    SENTI_WORDS_ = join(dirs.DATASETS_DIR, "sentifiles", "senti_.txt")
    NEG_WORDS = join(dirs.DATASETS_DIR, "sentifiles", "neg.txt")
    POS_WORDS = join(dirs.DATASETS_DIR, "sentifiles", "pos.txt")
    # 种子情感词典
    SEED_SENTIMENT_WORDS = join(dirs.DATASETS_DIR, "sentiment_words.txt")

    # 字体文件
    FONT_SIMHEI = join(dirs.FONTS_DIR, "simhei.ttf")

    # 词向量路径
    WORD2VEC_MODEL = join(dirs.DATASETS_DIR, "word2vec.model")

    # 聚类结果文件
    CLUSTER_DBSCAN_RESULT_CSV = join(dirs.RESULTS_DIR, "dbscan.csv")
    CLUSTER_DBSCAN_RESULT_EXCEL = join(dirs.RESULTS_DIR, "dbscan.xlsx")


if __name__ == "__main__":
    print(dirs.DATASETS_DIR)
