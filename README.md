原始lisa文件:https://github.com/danieluhricek/LiSa

解决build过程中一些下载问题

```
重新build遇到的主要问题：

1radare无法下载，到radareorg/radare2下载后COPY的镜像内。linux_images无法下载,到如下网站下载好COPY进去。
https://github.com/danieluhricek/linux-images/archive/v1.0.1.tar.gz
对于无法COPY的images，在.dockerignore中注释掉该行。

2无法安装r2pipe，将requirements.txt中版本改为1.5.3，进行build。
```