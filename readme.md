激活虚拟环境：
my_venv\Scripts\activate

---

运行：
(my_venv) D:\c_projects\Flask\241209_Flask\watchlist>flask run
flask run

执行 flask run 命令时，Flask 会使用内置的开发服务器来运行程序。
这个服务器默认监听本地机的 5000 端口，也就是说，我们可以通过在地址栏输入 http://127.0.0.1:5000 或是 http://localhost:5000 访问程序。

---

开启调试模式：

调试模式开启后，当程序出错，浏览器页面上会显示错误信息；代码出现变动后，程序会自动重载。

Win cmd ：set FLASK_DEBUG=1

---

程序发现机制

如果你把上面的程序 app.py 保存成其他的名字，比如 hello.py，接着执行 `flask run` 命令会返回一个错误提示。这是因为 Flask 默认会假设你把程序存储在名为 app.py 或 wsgi.py 的文件中。如果你使用了其他名称，就要设置系统环境变量 `FLASK_APP` 来告诉 Flask 你要启动哪个程序：

set FLASK_APP=hello.py
