# hlsdownloader
下载在线的m3u8到本地合并成ts文件

不支持直播下载

可下载伪装成图片流的在线hls流

采用pyaes进行ase解密，效率较低，可自行替换成其它aes库

需要暂停/继续下载功能，可以使用saveInfoToJson保存下载进度，loadInfoFromJson加载进度
