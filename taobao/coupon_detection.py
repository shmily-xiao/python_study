#!/usr/bin/env python
# -*- coding: utf-8 -*-


import wget
import requests

url = "https://uland.taobao.com/coupon/edetail?e=8enoEyP1lB8N%2BoQUE6FNzCt2r3C6nco47p9sN9KDqyFJAnz9kT0QCQgWm%2FfO0WDuKXH4Dp204Jn8UJYok44yznz%2F5lYwoL5ISB9Oxyt7%2BcDX18gaNN%2BIPporNYNlJ3NzEHNKdtmA%2FPZaEEz%2FJ22qjhezg1wrFfY3FlDJQsv%2B1e4%3D&af=1&pid=mm_128981071_39972563_150364908"

# target_url = "https://acs.m.taobao.com/h5/mtop.alimama.union.hsf.coupon.get/1.0/?jsv=2.4.0&appKey=12574478&t=1532509279642&sign=9b89027fcce75d03ed6519bbbbf9e4c4&api=mtop.alimama.union.hsf.coupon.get&v=1.0&AntiCreep=true&AntiFlood=true&type=jsonp&dataType=jsonp&callback=mtopjsonp2&data=%7B%22e%22%3A%228enoEyP1lB8N%2BoQUE6FNzCt2r3C6nco47p9sN9KDqyFJAnz9kT0QCQgWm%2FfO0WDuKXH4Dp204Jn8UJYok44yznz%2F5lYwoL5ISB9Oxyt7%2BcDX18gaNN%2BIPporNYNlJ3NzEHNKdtmA%2FPZaEEz%2FJ22qjhezg1wrFfY3FlDJQsv%2B1e4%3D%22%2C%22pid%22%3A%22mm_128981071_39972563_150364908%22%7D"

"""

https://acs.m.taobao.com/h5/mtop.alimama.union.hsf.coupon.get/1.0/?
    jsv=2.4.0
    &appKey=12574478
    
    &t=1532511294354  
    &sign=8248277be64f484a023962c4e879d173
    
    &api=mtop.alimama.union.hsf.coupon.get
    &v=1.0
    &AntiCreep=true
    &AntiFlood=true
    &type=jsonp
    &dataType=jsonp
    &callback=mtopjsonp2
    &data=%7B%22e%22%3A%22gQ966DhH1FwN%2BoQUE6FNzCt2r3C6nco47p9sN9KDqyFJAnz9kT0QCQgWm%2FfO0WDuIt%2B2DEi7tCuVMeZinZau8nz%2F5lYwoL5ISB9Oxyt7%2BcDX18gaNN%2BIPtgO3KjSp6FdxJfNlyXkD23hefsnlwqbgiOF3EJ1mxSuRW62oK5m7f4%3D%22%2C%22pid%22%3A%22mm_128981071_39972563_150364908%22%7D

{"e":"gQ966DhH1FwN+oQUE6FNzCt2r3C6nco47p9sN9KDqyFJAnz9kT0QCQgWm/fO0WDuIt+2DEi7tCuVMeZinZau8nz/5lYwoL5ISB9Oxyt7+cDX18gaNN+IPtgO3KjSp6FdxJfNlyXkD23hefsnlwqbgiOF3EJ1mxSuRW62oK5m7f4=","pid":"mm_128981071_39972563_150364908"}

old:
https://acs.m.taobao.com/h5/mtop.alimama.union.hsf.coupon.get/1.0/?jsv=2.4.0&appKey=12574478&t=1532511067112&sign=b61b999cb7f3a5700223ad0d0d5f60a3&api=mtop.alimama.union.hsf.coupon.get&v=1.0&AntiCreep=true&AntiFlood=true&type=jsonp&dataType=jsonp&callback=mtopjsonp1&data=%7B%22e%22%3A%22unqhzNrIPF8N%2BoQUE6FNzCt2r3C6nco47p9sN9KDqyFJAnz9kT0QCQgWm%2FfO0WDuASVLCTRR7AwcX5%2FO4Weuqnz%2F5lYwoL5IC0DytI6FkgSNR2k8djAjvIg4YhvdwHKtlg1lSgenbtyBnowgV5v6KZuTmXM9zXvK%22%2C%22pid%22%3A%22mm_128981071_39972563_150364908%22%7D
https://acs.m.taobao.com/h5/mtop.alimama.union.hsf.coupon.get/1.0/?jsv=2.4.0&appKey=12574478&t=1532509279642&sign=9b89027fcce75d03ed6519bbbbf9e4c4&api=mtop.alimama.union.hsf.coupon.get&v=1.0&AntiCreep=true&AntiFlood=true&type=jsonp&dataType=jsonp&callback=mtopjsonp2&data=%7B%22e%22%3A%228enoEyP1lB8N%2BoQUE6FNzCt2r3C6nco47p9sN9KDqyFJAnz9kT0QCQgWm%2FfO0WDuKXH4Dp204Jn8UJYok44yznz%2F5lYwoL5ISB9Oxyt7%2BcDX18gaNN%2BIPporNYNlJ3NzEHNKdtmA%2FPZaEEz%2FJ22qjhezg1wrFfY3FlDJQsv%2B1e4%3D%22%2C%22pid%22%3A%22mm_128981071_39972563_150364908%22%7D
https://acs.m.taobao.com/h5/mtop.alimama.union.hsf.coupon.get/1.0/?jsv=2.4.0&appKey=12574478&t=1532510902117&sign=624582b8085195af822fc92eab1542ca&api=mtop.alimama.union.hsf.coupon.get&v=1.0&AntiCreep=true&AntiFlood=true&type=jsonp&dataType=jsonp&callback=mtopjsonp1&data=%7B%22e%22%3A%2254PS3TEfQTAN%2BoQUE6FNzCt2r3C6nco47p9sN9KDqyFJAnz9kT0QCQgWm%2FfO0WDujHFe%2Fji3MW0QcvtLoqPS4Xz%2F5lYwoL5IC0DytI6FkgQtgMf7FUs3ubfxsi1c%2FlbUd3dYRnWQnO%2Bbg%2FMkcTHCkTNe5EyezcrR%22%2C%22pid%22%3A%22mm_128981071_39972563_150364908%22%7D

new:
https://acs.m.taobao.com/h5/mtop.alimama.union.hsf.coupon.get/1.0/?jsv=2.4.0&appKey=12574478&t=1532512981251&sign=569bb8d4f92cb36c113ca5359f74e8f6&api=mtop.alimama.union.hsf.coupon.get&v=1.0&AntiCreep=true&AntiFlood=true&type=jsonp&dataType=jsonp&callback=mtopjsonp1&data=%7B%22e%22%3A%2254PS3TEfQTAN%2BoQUE6FNzCt2r3C6nco47p9sN9KDqyFJAnz9kT0QCQgWm%2FfO0WDujHFe%2Fji3MW0QcvtLoqPS4Xz%2F5lYwoL5IC0DytI6FkgQtgMf7FUs3ubfxsi1c%2FlbUd3dYRnWQnO%2Bbg%2FMkcTHCkTNe5EyezcrR%22%2C%22pid%22%3A%22mm_128981071_39972563_150364908%22%7D


"""

HEADERS = {
    "authority": "acs.m.taobao.com",
    "method": "GET",
    "path": "/h5/mtop.alimama.union.hsf.coupon.get/1.0/?jsv=2.4.0&appKey=12574478&t=1532513807601&sign=820a8c3eee1dc0ef8b93536a33d4df4b&api=mtop.alimama.union.hsf.coupon.get&v=1.0&AntiCreep=true&AntiFlood=true&type=jsonp&dataType=jsonp&callback=mtopjsonp1&data=%7B%22e%22%3A%2270j3Bx7OhTEN%2BoQUE6FNzCt2r3C6nco47p9sN9KDqyFJAnz9kT0QCQgWm%2FfO0WDutNTUrfdfC1CbTDaeY22YE3z%2F5lYwoL5IC0DytI6FkgR2pj%2BrIzI8SMweCqqdVU5pfOdaPeFJvj2RMjz%2FiQJRwmSLnIuvFTVk%22%2C%22pid%22%3A%22mm_128981071_39972563_150364908%22%7D",
    "scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
    "cookie": "tracknick=w%5Cu6DD8%5Cu91D1%5Cu80051234; hng=CN%7Czh-CN%7CCNY%7C156; miid=603730700858829817; tg=0; cna=+6trEwII7V0CAXLwf1VT+4+V; thw=us; v=0; t=4516f02e83394ae88f3ace4cf07b25b9; cookie2=165b30715d4d039bf86bbfa517835ae5; _tb_token_=e859199ee31f4; skt=3da379287763e682; publishItemObj=Ng%3D%3D; csg=d98f201e; uc3=vt3=F8dBzrhPhemTCGGPpU0%3D&id2=UNGXFRPu1WA3&nk2=FFVXL4xI6gZ%2BR3k%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D; existShop=MTUzMjM2MjY3MQ%3D%3D; lgc=w%5Cu6DD8%5Cu91D1%5Cu80051234; _cc_=WqG3DMC9EA%3D%3D; dnk=w%5Cu6DD8%5Cu91D1%5Cu80051234; enc=Dy%2BM0eHyxIuKdgJ4rDK%2Fm1%2B7gEwiYH22DnToad4qcKxHXLxdA3aq%2FCRxH3Hb%2FwkVP%2FWkuEXZd3ol6wWuVf3lKA%3D%3D; uc1=cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&cookie21=W5iHLLyFeYZ1WM9hVnmS&cookie15=W5iHLLyFOGW7aA%3D%3D&existShop=false&pas=0&cookie14=UoTfKfQYuyrj5A%3D%3D&tag=8&lng=zh_CN; mt=ci=74_1; _m_h5_tk=29c616d915da44aa7499f5b3f9bffb5a_1532513634276; _m_h5_tk_enc=82582a3caa1e98dd9cf697fd63b0208d; isg=BFpa8Y-91Q3KqFjAioVZtRgrqwa8I95h9cpFymTTBu241_oRTBsudSAlo6PLHFb9",
    "cookie": "tracknick=w%5Cu6DD8%5Cu91D1%5Cu80051234; hng=CN%7Czh-CN%7CCNY%7C156; miid=603730700858829817; tg=0; cna=+6trEwII7V0CAXLwf1VT+4+V; thw=us; v=0; t=4516f02e83394ae88f3ace4cf07b25b9; cookie2=165b30715d4d039bf86bbfa517835ae5; _tb_token_=e859199ee31f4; skt=3da379287763e682; publishItemObj=Ng%3D%3D; csg=d98f201e; uc3=vt3=F8dBzrhPhemTCGGPpU0%3D&id2=UNGXFRPu1WA3&nk2=FFVXL4xI6gZ%2BR3k%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D; existShop=MTUzMjM2MjY3MQ%3D%3D; lgc=w%5Cu6DD8%5Cu91D1%5Cu80051234; _cc_=WqG3DMC9EA%3D%3D; dnk=w%5Cu6DD8%5Cu91D1%5Cu80051234; enc=Dy%2BM0eHyxIuKdgJ4rDK%2Fm1%2B7gEwiYH22DnToad4qcKxHXLxdA3aq%2FCRxH3Hb%2FwkVP%2FWkuEXZd3ol6wWuVf3lKA%3D%3D; uc1=cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&cookie21=W5iHLLyFeYZ1WM9hVnmS&cookie15=W5iHLLyFOGW7aA%3D%3D&existShop=false&pas=0&cookie14=UoTfKfQYuyrj5A%3D%3D&tag=8&lng=zh_CN; mt=ci=74_1; _m_h5_tk=21ea2817cc7830497e9855849b462852_1532516047165; _m_h5_tk_enc=273dc38a0218cd7635032fa8debf7036; isg=BE1NmZRBKnQ1Ho854USWfDNaXG8HgoH4rpvyE4_Si-RThm04V3qRzJsU9FpFRpm0",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
}

target_url= "https://acs.m.taobao.com/h5/mtop.alimama.union.hsf.coupon.get/1.0/?jsv=2.4.0&appKey=12574478&t=1532513807601&sign=820a8c3eee1dc0ef8b93536a33d4df4b&api=mtop.alimama.union.hsf.coupon.get&v=1.0&AntiCreep=true&AntiFlood=true&type=jsonp&dataType=jsonp&callback=mtopjsonp1&data=%7B%22e%22%3A%2270j3Bx7OhTEN%2BoQUE6FNzCt2r3C6nco47p9sN9KDqyFJAnz9kT0QCQgWm%2FfO0WDutNTUrfdfC1CbTDaeY22YE3z%2F5lYwoL5IC0DytI6FkgR2pj%2BrIzI8SMweCqqdVU5pfOdaPeFJvj2RMjz%2FiQJRwmSLnIuvFTVk%22%2C%22pid%22%3A%22mm_128981071_39972563_150364908%22%7D"
r = requests.get(target_url,  headers=HEADERS)
print r.text