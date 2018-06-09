from gmail import *
from random import choice
html_content = """
<p style="text-align: center;">Cộng h&ograve;a x&atilde; hội chủ nghĩa Việt Nam</p>
<p style="text-align: center;">Độc lập - Tự do - Hạnh ph&uacute;c</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;"><strong>ĐƠN XIN NGHỈ HỌC</strong></p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: left;">K&iacute;nh gửi: Giảng vi&ecirc;n lớp C4E18.</p>
<p style="text-align: left;">T&ecirc;n em l&agrave;: Đ&ocirc;ng.</p>
<p style="text-align: left;">H&ocirc;m nay em bị {{sickness}} n&ecirc;n xin thầy cho em nghỉ một buổi</p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">Đ&ocirc;ng</p>"""

#placeholder
sickness = ["đau bụng", "trĩ", "ốm"]
new_sickness = choice(sickness)
new = html_content.replace("{{sickness}}", new_sickness)

gmail = GMail('dongkooi01@gmail.com', 'ngodong97')
msg = Message('Test Message', to = 'nvhoang00010@gmail.com', html = new)
gmail.send(msg)
