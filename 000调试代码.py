import logging

logging.disable(logging.CRITICAL)  #是否进行debug调试
#是否保存日志文件
#logging.basicConfig(filename='log_file.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')
pass
logging.debug('End of program')
