class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        i=0
        while dividend != 0:
            if abs(dividend)<abs(divisor):
                return 0
                break

            if (divisor<0 and dividend < 0) or (divisor >0 and dividend > 0):
                if abs(divisor)==1:
                    if dividend == -2147483648:
                        return 2147483647
                    return abs(dividend)
                    break
                temp=abs(divisor)
                mult=1
                while abs(dividend)>=(temp<<1):
                    temp<<=1
                    mult<<=1
                if dividend<0:
                    dividend+=temp
                else:
                    dividend-=temp
                i+=mult
                if abs(dividend)<abs(divisor):
                    dividend-=dividend

            else:
                if abs(divisor)==1:
                    if dividend<0:
                        return dividend
                    else:
                        return -dividend
                    break
                temp=abs(divisor)
                mult=1
                while abs(dividend)>=(temp<<1):
                    temp<<=1
                    mult<<=1
                if dividend<0:
                    dividend+=temp
                else:
                    dividend-=temp
                i-=mult
                if abs(dividend)<abs(divisor):
                    dividend=abs(dividend)-abs(dividend)

        return i
