
# SCDV�ɂ��x�N�g���\����p�������͊Ԃ̎Q�ƃl�b�g���[�N����  

��ҁFkonkon

## �T�v

���͓��m�̑��݊֌W���A���ꂼ��̕��̕\���x�N�g����cos�ގ��x�Ŕ�r���ĎQ�Ɗ֌W���l�b�g���[�N������v���O�����B  
�v����ɕ��͊Ԃ̑��ݎQ�Ɗ֌W(���R�s�y�֌W)�����������B

## �����

������͈ȉ��̒ʂ�B  

OS Windows10 64bit  
CPU Intel i7-7700  
GPU NVIDIA GeForce GTX1070  
Memory: 16 GB  

Python�y�ѕK�v�p�b�P�[�W�̃o�[�W�����͈ȉ��̒ʂ�ł��B  
  
Python == 3.6.5  
numpy==1.14.5  
pandas==0.23.1  
matplotlib==2.2.2  
mecab-python-windows==0.996.1  
networkx==2.3  
python-docx==0.8.10  
gensim==3.4.0  
scikit-learn==0.19.1  
  
environments.txt�ɕK�v�ȃp�b�P�[�W(MeCab�ȊO)�͋L�ڂ��Ă���܂��B  
�ȉ��̂悤�ɂ܂Ƃ߂ăC���X�g�[���ł��܂��B  
  
�@$ pip install -r environments.txt  

Mecab�̃C���X�g�[�����@�͈ȉ����Q�Ƃ��Ă��������B  
[Python��MeCab�Ō`�ԑf���(on Windows) --Qiita](https://qiita.com/menon/items/f041b7c46543f38f78f7)  

## �g����

1. document/�ɁA���|�[�g����([�w�Дԍ�].docx)�����Ă��������B.doc(�Â�Word�̕ۑ��`��)�ɂ͑Ή����Ă܂���B.docx�ɕϊ����Ă������Ă��������B  

2. ���O�w�K���f����p�ӂ��Ă��������B������[�����M�R�[�|���[�V����](http://aial.shiroyagi.co.jp/2017/02/japanese-word2vec-model-builder/)���񂩂�_�E�����[�h���܂����B�𓀌�o�Ă����t�@�C���͂��ׂ� pretrained_model/�̒��ɓ���Ă��������B  

3. �R�}���h�v�����v�g���J���A��L�̃p�b�P�[�W���C���X�g�[�����ꂽPython����L���ɂ��Ă��������B

4. ���̃f�B���N�g��(CopyPasteNetwork/) �Ɉړ����A�ȉ��̃R�}���h�Ńv���O���������s���܂��B  
  
�@�@$ python main.py document [threshold]  
  
�@�@threshold�ɂ͊֘A���𔻕ʂ���cos�ގ��x��臒l(0~1)����͂��Ă��������B0.8���x�𐄏����܂��B  

5. �͂��߂ăv���O���������s����ꍇ�͎��O�w�K���f���ɑ΂��Ēǉ��w�K���s���܂��B�ǉ��w�K��̃��f���� model/ �ɕۑ�����܂��B��x�ڈȍ~�Ƀv���O���������s���Amodel�Ɋw�K���f�������݂���ꍇ�͒ǉ��w�K���s���܂���B  

6. ���o���ꂽ�l�b�g���[�N�\����  
  
	result_(sim=[threshold]).csv  
	network_(sim=[threshold]).json  
  
�@�@�Ƃ��ĕۑ�����܂��B  
�@�@���Ƃ͎ς�Ȃ�Ă��Ȃ�D���ɂǂ����B  

7. JSON�t�@�C���̓O���t�`��\�t�g[Cytoscape](https://cytoscape.org/)�ŊJ���܂��B�T���v���͈ȉ��B

## �l�b�g���[�N�}�T���v��

<img src="sample(sim=0.80).png">

threshold == 0.8�̏ꍇ�̃l�b�g���[�N�}  

<img src="sample(sim=0.60).png">

threshold == 0.6�̏ꍇ�̃l�b�g���[�N�}  
�G�b�W�̃A���t�@�l�����̗ގ��x�A�m�[�h�̃T�C�Y�����ݎQ�Ƃ̐���\���B  
(�l�b�g���[�N�}��Cytoscape�ɂč쐬)  

## �f�B���N�g���\��

CopyPasteNetwork/ (����)
��  
�� document/ (�w�K, ��͑Ώۂ�.docx�h�L�������g��ۑ�)  
���@��  
���@�� ********.docx  
���@�� ********.docx  
���@�@�@�F  
��  
�� pretrained_model/ (���O�w�K���f���͂����ɓ����)  
���@��  
���@�� word2vec.gensim.model  
���@�� word2vec.gensim.model.syn1neg.npy  
���@�� word2vec.gensim.model.wv.syn0.npy  
��  
���@��[http://aial.shiroyagi.co.jp/2017/02/japanese-word2vec-model-builder/]  
���@�@����_�E�����[�h  
��  
�� model/ (�Ċw�K����Word2Vec���f���͂����ɓ���)  
���@��  
���@�� *****.model  
���@�� *****.syn1neg.npy  
���@�� *****.wv.syn0.npy  
��  
�� stopword.txt  
�� ���͉�͂̍ۂɕs�K�v�ƂȂ���̃��X�g�B(��F�H�w������)  
�� �K�v�ɉ����ď��������Ă��������B  
��  
�� environment.txt  
�� �K�v�ƂȂ�Python�p�b�P�[�W�̃��X�g�ł��B  
��  
�� readme.txt  
�@ ���̃e�L�X�g�ł��B  
  

���: konkon

Twitter: https://twitter.com/konkon28983820  
E-mail: velvetteen.rabbit@gmail.com  
GitHub: https://github.com/konkon3249  
Qiita: https://qiita.com/kon2  

Copyright (c) 2019 konkon. 