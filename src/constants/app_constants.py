from os.path import join as join_path

KALDI_PATH_FILE = './kaldi/path.sh'
KALDI_QUEUE_FILE = './kaldi/queue.pl'

DATA_DIR = 'data'
EMB_DIR = 'embeddings'
LOGS_DIR = 'logs'
MFCC_DIR = 'mfcc'
MODELS_DIR = 'models'
PLDA_DIR = 'plda'
VAD_DIR = 'vad'
TMP_DIR = 'tmp'

TRAIN_SPLIT = 'train'
DEV_SPLIT = 'dev'
ENROLL_SPLIT = 'enroll'
UNLABELLED_SPLIT = 'unlabelled'
TEST_SPLIT = 'test'

LATEST_MODEL_FILE = 'latest.json'

DATA_SCP_FILE = join_path(DATA_DIR, 'data.scp')
EMB_SCP_FILE = join_path(DATA_DIR, 'embeddings.scp')
FEATS_SCP_FILE = join_path(MFCC_DIR, 'feats.scp')
UTT2NUM_FRAMES_FILE = join_path(MFCC_DIR, 'utt2num_frames')
VAD_SCP_FILE = join_path(VAD_DIR, 'vad.scp')
TMP_SCP_FILE = join_path(TMP_DIR, 'tmp.scp')

NUM_UTT_FILE = join_path(DATA_DIR, 'num_utt')
SPK_UTT_FILE = join_path(DATA_DIR, 'spk2utt')
TRIALS_FILE = join_path(DATA_DIR, 'trials')
UTT_SPK_FILE = join_path(DATA_DIR, 'utt2spk')

SCORES_FILE = 'score.txt'
EER_INPUT_FILE = 'eer_input.txt'
