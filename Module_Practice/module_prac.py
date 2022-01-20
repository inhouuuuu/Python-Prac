#영화관 모듈 예시

# import theater_module
# theater_module.price(3) # 3명이서 영화 보러갈때 가격
# theater_module.price_morning(4) # 4명이서 조조할인 영화보러갈때 가격
# theater_module.price_solider(5) # 군인 영화 가격

# import theater_module as mv #모듈 별명 호출
# mv.price(3)
# mv.price_morning(4)
# mv.price_solider(5)

# from theater_module import * #모듈 전체 호출
# price(3)
# price_morning(4)
# price_morning(5)

# from theater_module import price_morning, price #필요한 부분만 가져오기
# price(5)
# price_morning(6)

from Module_Practice.theater_module import price_solider as price
price(5)