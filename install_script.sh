//Program image to SD card on mac
#>diskutil list  //get the sd card name, for example /dev/disk4
#>diskutil unmountDisk /dev/disk4
#>sudo dd if=Documents/PYNQ/PYNQ-Z2-image/pynq_z2_v2.6.0.img of=/dev/disk4 bs=20m

// 同步时区
 timedatectl set-timezone "Asia/Shanghai"

// install gunicorn
sudo pip3 install gunicorn

//安装 postgresql
sudo apt-get install postgresql postgresql-client
//安装psycopg2
sudo apt-get install libpq-dev python-dev
sudo apt-get install python-psycopg2
sudo pip3 install psycopg2-binary
sudo pip3 install psycopg2


//创建数据库
1 登陆 psql
sudo -u postgres psql

2 创建用户
create user xilinx with password 'xilinx';

3 为用户创建数据库
create database powerdb owner xilinx;

4 授权
grant all privileges on database powerdb to xilinx;

5 登陆
psql -U xilinx -d powerdb -h 127.0.0.1 -p 5432
