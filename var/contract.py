# -*- coding: utf-8 -*-

class contract():
    종목코드 = ''
    매도?��구분 = ''
    ?��?�� = 0
    체결?��?���?�? = 0
    ?��?���? = [0]
    ?��?���? = [0]

    def __init__(self, params):
        if '종목코드' in params: self.종목코드 = params['종목코드']
        if '매도?��구분' in params: self.매도?��구분 = params['매도?��구분']
        if '?��?��' in params: self.?��?�� = params['?��?��']
        if '체결?��?���?�?' in params: self.체결?��?���?�? = params['체결?��?���?�?']
        if '?��?���?' in params: self.?��?���? = params['?��?���?']
        if '?��?���?' in params: self.?��?���? = params['?��?���?']