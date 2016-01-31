#!/usr/bin/python
# -*- coding: utf8 -*-

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.core.window import Window

TEXT = '''Câu 1: Trong mô hình OSI, thiết bị bridge làm việc tại tầng nào sau đây:
A. Session
B. Network
C. Transport
---D. Data link
'http://sinhvienit.net/forum/hub-repeater-router-switch-bridge-gateway-la-gi.7192.html'

Câu 2: Tấn công mạng nào sau đây lợi dụng điểm yếu trong chức năng tái lắp ghép phân mảnh gói dữ
liệu trong bộ giao thức TCP/IP:
---A. Teardrop
B. Smurf
C. Ping of death
D. SYN flood
'http://en.wikipedia.org/wiki/IP_fragmentation_attack'

Câu 3: Mô hình điểu khiển truy cập nào dưới đây sử dụng ACL (Access Control Lists) để xác định
quyền hạn của người dùng đối với một tài nguyên:
A. MAC
B. RBAC
---C. DAC
D. Không có mô hình nào cả

Câu 4: Giao thức đường hầm nào sau đây hỗ trợ bao gói (encapsulation) trong môi trường kết nối
đơn điểm-tới-điểm (point-to-point)?
A. PPTP
B. L2F
C. L2TP
D. SSH

Câu 5: Loại tấn công nào sau đây cung cấp cho tin tặc những thông tin hữu ích về các dịch vụ chạy trong
hệ thống:
A. Session Hijacking
---B. Port scan
C. Dumpster diving
D. IP sweep

Câu 6: Mô hình an toàn dựa trên mô hình lưới (lattice) được dùng để:
A. Loại bỏ các thuộc tính không hợp hệ
B. Ngăn các luồng thông tin không hợp hệ giữa các thực thể
C. Chống lại các truy cập trái phép
D. Quản lý người dùng

Câu 7: Thứ tự các giao thức làm việc trên các tầng application, data link, network, transport tương
ứng với phương án nào sau đây:
---A. FTP, ARP, TCP, UDP
B. FTP, ICMP, IP, UDP
---C. TFTP, ARP, IP, UDP
D. TFTP, RARP, IP, ICMP
'ICMP - network'

Câu 8: Những đặc tính nào sau đây có thể được sử dụng để phân biệt sự khác nhau giữa worm và
virus
A. Worm nhiễm vào hệ thống bằng cách ghi đè dữ liệu lên bản ghi Master Boot của thiết bị lưu trữ (ổ
cứng, ổ mềm vv...)
B. Worm lây nhiễm từ hệ thống này sang hệ thống khác mà không cần sự tác động của người dùng
C. Worm luôn có mã độc để để phá hoại hệ thống đã bị nhiễm
---D. Tất cả những đặc tính trên

Câu 9: Khi tắt đi hai dịch vụ không cần sử dụng là chargen và echo. Việc làm này làm giảm đi khả năng
của tấn công nào sau đây:
A. Smurf
B. Land
---C.Fraggle
D.Ping of death
'http://www-arc.com/sara/cve/Possible_DoS_problem.html'

Câu 10: Thành phần an toàn nào sau đây được cho là thành phần an toàn vật lý:
A. VPN Tunnel
---B. Mantrap
C. Bastion host
D. IPSec
'http://en.wikipedia.org/wiki/Bastion_host'

Câu 11: Khi phát hiện có kẻ xâm nhập vào hệ thống, thì hành động nào sao đây nên được thực hiện
đầu tiên?
A. Xác định danh tính kẻ xâm nhập
B. Gửi trực tiếp các file nhật ký cho các chuyên gia chống tội phạm máy tính (forensic expert) để phân
tích.
C. Xóa sạch các file nhật ký để có thể thu được các dữ liệu cụ thể khi có các cuộc tấn khác xảy ra
---D. Gửi tất cả các file nhật ký cho các chuyên gia chống tội phạm máy tính thông qua trung gian.

Câu 12: Giải pháp backup nào sau đây thường được dùng để bảo vệ dữ liệu cho các doanh nghiệp nhỏ?
A. Site redundancy
B. Offsite, secure recovery
C. Onsite backup
D. High availability systems

Câu 13: Phát biểu nào sau đây là không đúng về giao thức SOCKS:
A. Nó được xem là phần mềm mức ứng dụng
B. Nó sử dụng ESP để xác thực và lập mã
C. Nó vận hành tại tầng vận tải của mô hình OSI
D. Các ứng dụng mạng cần phải sử dụng giao thức SOCKS để vận hành

Câu 14: Hệ thống phát hiện xâm nhập (IDS-Intrusion Detection System) nào có thể theo dõi được người
sử dụng và hành vi mạng:
A. Thống kê (Statistical)
B. Dựa trên dấu hiệu (Signature-based)
C. Tĩnh (Static)
D. Dựa trên máy chủ (Host-based)

Câu 15: Mô hình an toàn nào sau đây cài đặt các ma trận kiểm soát truy cập để kiểm soát xem các
chủ thể tương tác với các đối tượng như thế nào:
A. Bắt buộc (Mandatory)
B. Tập trung (Centralized)
C. Phi tập trung (Decentralized)
D. Tuỳ ý (Discretionary)'''

class AutoLineBreakLabel(GridLayout):
	def __init__(self, text, width = 300, markup = True, valign = 'top', halign = 'left', **kwargs):
		super(AutoLineBreakLabel, self).__init__(**kwargs)
		self.size_hint = (None, None)
		self.width = width
		self.cols = 1
		self.pos_hint = {'center_x' : .5, 'center_y' : .5}
		self.bind(minimum_height = self.setter('height'))
		self.label = Label(text = text, size_hint = (1, None), halign = halign, valign = valign, markup = markup)
		self.label.bind(width = lambda obj, value:
							self.label.setter('text_size')(obj, (value, None)))
		self.label.bind(texture_size = self.label.setter('size'))
		self.add_widget(self.label)

class ScrollViewLabel(ScrollView):
	def __init__(self, text, width = 300, pos_hint = {'center_x' : .5, 'center_y' : .5}, **kwargs):
		super(ScrollViewLabel, self).__init__(**kwargs)
		self.size_hint = (None, 1)
		self.width = width
		self.pos_hint = pos_hint
		self.do_scroll_x = False
		self.add_widget(AutoLineBreakLabel(text= text, width = width))

class testApp(App):
	def build(self):
		f = FloatLayout()
		s = ScrollViewLabel(text = TEXT, width = 600, pos_hint = {'right' : 1, 'top' : 1})
		f.add_widget(s)
		return f

if __name__ == '__main__':
	testApp().run()
