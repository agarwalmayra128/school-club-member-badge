member_name = input("enter the member_name:")
club_name = input("enter the club _name:")
member_number = 8
points = 9.5
is_active = True
print(type(member_name))
print(type(club_name))
print(type(member_number))
print(type(points))
print(type(is_active))
badge_code = member_name[0:3] + club_name[-1] + str(member_number) 
print(badge_code)
print("===CLUB BADGE===")
print("member name is :", member_name)
print("club name is :", club_name)
print("points are : ", points)
print("active is : " , is_active)
print("badge code is : ", badge_code)


