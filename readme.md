
------------------------------------------------------------------------------  
  
�@�@SCDV�ɂ��x�N�g���\����p�����w�����|�[�g�Ԃ̎Q�ƃl�b�g���[�N����  
  
------------------------------------------------------------------------------  

��ҁFkonkon

# �T�v

���͓��m�̑��݊֌W���A���ꂼ��̕��̕\���x�N�g����cos�ގ��x�Ŕ�r���ĎQ�Ɗ֌W���l�b�g���[�N������v���O�����B  
�v����ɕ��͊Ԃ̑��ݎQ�Ɗ֌W(���R�s�y�֌W)�����������B

# �����

������͈ȉ��̒ʂ�B  

OS Windows10 64bit  
CPU Intel i7-7700  
GPU NVIDIA GeForce GTX1070  
Memory: 16 GB  

Python�y�ѕK�v�p�b�P�[�W�̃o�[�W�����͈ȉ��̒ʂ�ł��B  
  
Python == 3.6.7  
numpy == 1.16.4  
matplotlib == 3.1.1  
  
environments.txt�ɕK�v�ȃp�b�P�[�W�͋L�ڂ��Ă���܂��B  
�ȉ��̂悤�ɂ܂Ƃ߂ăC���X�g�[���ł��܂��B  
  
�@$ pip install -r environments.txt  

# �g����

1. document/�ɁA���|�[�g����([�w�Дԍ�].docx)�����Ă��������B  
�@�@.doc(�Â�Word�̕ۑ��`��)�ɂ͑Ή����Ă܂���B.docx�ɕϊ����Ă������Ă��������B  

2. ���O�w�K���f����p�ӂ��Ă��������B  
�@�@(�����͂���[http://aial.shiroyagi.co.jp/2017/02/japanese-word2vec-model-builder/]�̂��_�E�����[�h���܂���)  
�@�@�𓀌�o�Ă����t�@�C���͂��ׂ� pretrained_model/�̒��ɓ���Ă��������B  

3. �R�}���h�v�����v�g���J���A��L�̃p�b�P�[�W���C���X�g�[�����ꂽPython����L���ɂ��Ă��������B  

4. ���̃f�B���N�g��(CopyPasteNetwork/) �Ɉړ����A�ȉ��̃R�}���h�Ńv���O���������s���܂��B  
  
�@�@$ python main.py document [threshold]  
  
�@�@threshold�ɂ͊֘A���𔻕ʂ���cos�ގ��x��臒l(0~1)����͂��Ă��������B0.8���x�𐄏����܂��B  

5. �͂��߂ăv���O���������s����ꍇ�͎��O�w�K���f���ɑ΂��Ēǉ��w�K���s���܂��B  
�@�@�ǉ��w�K��̃��f���� model/ �ɕۑ�����܂��B  
�@�@��x�ڈȍ~�Ƀv���O���������s���Amodel�Ɋw�K���f�������݂���ꍇ�͒ǉ��w�K���s���܂���B  

6. ���o���ꂽ�l�b�g���[�N�\����  
  
	result_(sim=[threshold]).csv  
	network_(sim=[threshold]).json  
  
�@�@�Ƃ��ĕۑ�����܂��B  
�@�@���Ƃ͎ς�Ȃ�Ă��Ȃ�D���ɂǂ����B  
�@�@JSON�t�@�C���̓t���[�̃O���t�`��\�t�gCytoscape(https://cytoscape.org/)�ɃC���|�[�g�\�Ȍ`���ŕۑ�����܂��B  


# �f�B���N�g���\��

CopyPasteNetwork/  
��  
�� document/ (�w�K, ��͑Ώۂ�.docx�h�L�������g��ۑ�)  
���@��  
���@�� ********.docx  
���@�� ********.docx  
���@�@�@�F  
��  
�� pretrained_model/ (���O�w�K���f����ۑ�)  
���@��  
���@�� word2vec.gensim.model  
���@�� word2vec.gensim.model.syn1neg.npy  
���@�� word2vec.gensim.model.wv.syn0.npy  
��  
���@��[http://aial.shiroyagi.co.jp/2017/02/japanese-word2vec-model-builder/]  
���@�@����_�E�����[�h  
��  
�� model/ (�Ċw�K����Word2Vec���f����ۑ�)  
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
  
�Q�l�l�l�l�l�l�l�l�l�l�l�l�l�l�l�l�l�l�l�l�l�l�l�l�l�l�l�l�l�l�Q  
���@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@��  
���@�@�@�@�@�@�@���: �ΐ�W�� (a.k.a. konkon)�@�@�@�@�@�@�@�@��  
���@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@��  
���@�@�@Twitter: https://twitter.com/konkon28983820 �@�@�@�@�@��  
���@�@�@E-mail: ishikawa@unno.material.nagoya-u.ac.jp�@�@�@�@ ��  
���@�@�@GitHub: https://github.com/konkon3249�@�@�@�@�@�@�@�@ ��  
���@�@�@Qiita: https://qiita.com/kon2�@�@�@�@�@�@�@�@�@�@�@�@ ��  
���@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@��  
�PY^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^�P  
  
Copyright (c) 2019 Kohei Ishikawa  