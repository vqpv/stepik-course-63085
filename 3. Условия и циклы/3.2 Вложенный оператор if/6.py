s, v_1, v_2, t_1, t_2 = map(int, input().split())

st_1 = s * v_1 + 2 * t_1
st_2 = s * v_2 + 2 * t_2

if st_2 > st_1:
    print('First')
elif st_2 < st_1:
    print('Second')
elif st_1 == st_2:
    print('Friendship')
