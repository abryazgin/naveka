
# -------------------------------------
# preinstall
# -------------------------------------
  
  <install python>
  sudo pip install django
  
# -------------------------------------
# download
# -------------------------------------
  
  git clone https://github.com/bryazginnn/naveka.git
  
  
# -------------------------------------
# mysql
# -------------------------------------
  
  CREATE DATABASE naveka CHARACTER SET utf8 COLLATE utf8_general_ci;
  CREATE USER 'naveka'@'localhost' IDENTIFIED BY '1';
  GRANT ALL PRIVILEGES ON naveka . * TO 'naveka'@'localhost';
  FLUSH PRIVILEGES;

# -------------------------------------
# run server
# -------------------------------------
  
  python manage.py migrate