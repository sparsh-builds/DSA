# Dutch National Flag

def sort012(arr):
        # code here
        l=0
        h=len(arr)-1
        m=0
        
        while(m<=h):
            if arr[m]==0:
                arr[l],arr[m]=arr[m],arr[l]
                
                m+=1
                l+=1
            elif arr[m]==1:
                m+=1
            else: # arr[m]==2
                arr[h],arr[m]=arr[m],arr[h]
                h-=1
if __name__ == "__main__":
        arr=[0,1,2,0,1,2]
        sort012(arr)
        print(arr)