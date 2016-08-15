class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def outputer_html(self)    :
        fout = open('outputer_html', 'w')

        font.write('<html>')
        font.write('<body>')
        font.write('<table>')

        # ascii python 默认编码
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'].encode('utf-8'))
            fout.write('<td>%s</td>' % data['summary'].encode('utf-8'))
            fout.write('</tr>')

        font.write('</table>')
        font.write('</body>')
        font.write('</html>')

        fout.close()
