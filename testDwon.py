from hlsDownloader import hlsDownloader
import time

urls =  [
            'https://rb.sszyplay.com/20220516/zmw0CsiO/index.m3u8',
            'https://qq.sd-play.com/20220513/MzTx2HAj/index.m3u8',
            'https://vip.lz-cdn11.com/20220524/7402_d61ffbf2/index.m3u8',
            'https://vod1.kczybf.com/20220508/t9lrdj2h/index.m3u8',
            'https://g.gszyvv.com:65/20220522/iGkaJBCv/index.m3u8'
        ]

if __name__ == '__main__':
    downlist = []
    n = 0
    for url in urls:
        downloader =  hlsDownloader()
        downloader.openM3u8Url(url)
        n = n + 1
        downloader.downToFile('d:\\ts\\' + str(n) + '.ts')
        downlist.append(downloader)
    listlen = len(downlist)
    n = 0
    x = 0
    while True:
        m = 0
        for downloader in downlist:
            if downloader.downstate == 0:
                xzzt = '未开始'
            if downloader.downstate == -1:
                xzzt = '已暂停'
            if downloader.downstate == 1:
                xzzt = '下载中'
            if downloader.downstate == 2:
                xzzt = '已下载'
            newinfo = {'hlsname':downloader.medianame,'hlsdowned':downloader.downpercent,'successed':downloader.downedsuccess,'hlsstates':xzzt}
            print(newinfo)
            if downloader.downstate == 2 or downloader.downstate == -1:
                m = m + 1
        if m == listlen:
            break;
        n = n + 1
        if n == 5:
            downlist[0].stop()
        if n == 10:
            downlist[1].stop()
        if n == 15:
            downlist[2].stop()
        if n == 20:
            downlist[3].stop()
        if n == 25:
            downlist[4].stop()
        print('=======================================================================')
        time.sleep(1)
    print('---------')
    #del downloader