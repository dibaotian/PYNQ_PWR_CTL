// 同步时区
 timedatectl set-timezone "Asia/Shanghai"




//安装 postgresql
sudo apt-get install postgresql postgresql-client
//安装psycopg2
sudo apt-get install libpq-dev python-dev
pip3 install psycopg2-binary


//创建数据库
1 登陆 psql
sudo -u postgres psql

2 创建用户
create user xilinx with password 'xilinx';

3 为用户创建数据库
create database powerdb owner xilnx;

4 授权
grant all privileges on database powerdb to xilinx;

5 登陆
psql -U xilinx -d powerdb -h 127.0.0.1 -p 5432
