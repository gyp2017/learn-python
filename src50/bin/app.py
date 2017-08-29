# -*- coding: utf-8 -*-
# 50 처음 만드는 웹사이트
# 51 웹 브라우저에서 입력 받기

import web

urls = (
    '/hello', 'index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

class index(object):
    def GET(self):
        return render.hello_form_laid_out()

    def POST(self):
        form = web.input(name="Nobody", greet="Hello")
        greeting = "%s, %s" % (form.greet, form.name)

        return render.index_laid_out(greeting = greeting)

if __name__ == "__main__":
    app.run()
