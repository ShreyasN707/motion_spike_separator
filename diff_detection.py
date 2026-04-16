import cv2

# img1=cv2.imread('fb1.png')
# img2=cv2.imread('fb2.png')


def diff_calculator(img1,img2):
    
    img2=cv2.resize(img2,(img1.shape[1],img1.shape[0]))
    
    gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

    gray1=cv2.GaussianBlur(gray1,(5,5),0)
    gray2=cv2.GaussianBlur(gray2,(5,5),0)

    edges1=cv2.Canny(gray1,50,150)
    edges2=cv2.Canny(gray2,50,150)

    diff = cv2.absdiff(edges1, edges2)

    _, thresh = cv2.threshold(diff, 100, 255, cv2.THRESH_BINARY)

    change_ratio=(thresh>0).sum()/thresh.size

    print(change_ratio)

    if change_ratio < 0.04:
        print("No motion or just movment")

    elif change_ratio < 0.1:
        return 'motion'

    elif change_ratio < 0.2:
        print('motion')
        return 'motion'

    else:
        return 'motion'

# diff_calculator(img1,img2)