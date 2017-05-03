from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams

#获取文档对象
fp = open('/Users/zhumi/Desktop/2017_04_24_pm_5796ef7b-fcdf-4c57-ba85-962fe06c03ac_17041416.pdf', 'rb')

#创建一个与文档关联的解释器
parser = PDFParser(fp)

#创建PDF文档对象
doc = PDFDocument()

#链接解释器和文档对象
parser.set_document(doc)
doc.set_parser(parser)

#初始化文档,如果PDF文档带有密码则传入
doc.initialize('')

#穿件PDF资源管理器
resource = PDFResourceManager()

#参数分析器
laParams = LAParams()

#创建聚合器
device = PDFPageAggregator(resource, laparams=laParams)

#页面解释器
interpreter = PDFPageInterpreter(resource, device)

#使用文档对象得到页面的集合
for page in doc.get_pages():
	#使用页面解释器来读取
	interpreter.process_page(page)

	#使用聚合器来获得内容
	layout = device.get_result()

	for out in layout:
		if hasattr(out, 'get_text'):
			print(out.get_text())










