FROM registry.cn-zhangjiakou.aliyuncs.com/dvadmin-pro/python38-base-backend:latest
WORKDIR /backend
COPY ./backend/ .
RUN awk 'BEGIN { cmd="cp -i ./conf/env.example.py   ./conf/env.py "; print "n" |cmd; }'
RUN python3 -m pip install  -r requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
CMD ["/backend/docker_start.sh"]
