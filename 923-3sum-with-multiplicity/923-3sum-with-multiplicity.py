class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        mod=10**9+7
        counter=Counter(arr)
        keys=sorted(counter)
        disNum=len(keys)
        result=0
        for first,numOne in enumerate(keys):
            second,third=first,disNum-1
            temp=target-numOne
            while second<=third:
                numTwo,numThree=keys[second],keys[third]
                if numTwo+numThree>temp:
                    third=third-1
                elif numTwo+numThree<temp:
                    second=second+1
                else:
                    if first<second<third:
                        result+=counter[numOne]*counter[numTwo]*counter[numThree]
                    elif first<second==third:
                        result+=counter[numOne]*(counter[numThree]-1)/2*counter[numTwo]
                    elif first==second<third:
                        result+=counter[numOne]*(counter[numTwo]-1)/2*counter[numThree]
                    else:
                        result+=counter[numOne]*(counter[numTwo]-1)*(counter[numThree]-2)/6
                    second=second+1
                    third=third-1
        return int(result%mod)