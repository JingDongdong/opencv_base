import cv2
def show_save(name,img):
    while True:
        cv2.imshow(name,img)
        key = cv2.waitKey(0)
        if key & 0xFF == ord('q'):
            print('1')
            break
        elif key & 0xFF == ord('s'):
            cv2.imwrite('./test.png',img)
            print('2')
            break
        else:
            print(key)
    cv2.destroyAllWindows()

