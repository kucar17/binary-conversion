import cv2
import numpy as np

# This function receives an image and also a bitPlaneNumber (default 8 for 8-bit images) to perform Bit Level Slicing.
# After the opeation, function records the bitlevel sliced image to the working directory.
def bitPlaneSlice(inimg, bitPlaneNumber=8):
    #print(bin(inimg[300][200])[2:].zfill(8))
    binaryArray = np.zeros((inimg.shape[0], inimg.shape[1]))
    # Finding the binary equivalent values of each pixel in the image
    # split method is used to remove the leading "0b" from the binary string.
    for j in range(0, inimg.shape[0]):
        for k in range(0, inimg.shape[1]):
            binaryArray[j][k] = bin(inimg[j][k])[2:].zfill(8)
            #print(bin(inimg[j][k]).split("b")[1].zfill(8))
            #print(bin(inimg[j][k]).split("b")[1][1])

    #print(type(str(binaryArray[0][0])))
    #print(str(binaryArray[0][0])[1])
    #print(int(str(binaryArray[0][0])[1]))
    #print(str(binaryArray[0][0].split(".")[1]))
    # Initializing the bitPlaneImg (will change after each bit scan)
    bitPlaneImg = np.zeros((inimg.shape[0], inimg.shape[1]), dtype=str)

    print(inimg[354][587])
    print(bin(inimg[354][587])[2:].zfill(8))
    print(bin(inimg[354][587])[2:].zfill(8)[0])
    print(bin(inimg[354][587])[2:].zfill(8)[1])
    print(bin(inimg[354][587])[2:].zfill(8)[2])
    print(bin(inimg[354][587])[2:].zfill(8)[3])
    print(bin(inimg[354][587])[2:].zfill(8)[4])
    print(bin(inimg[354][587])[2:].zfill(8)[5])
    print(bin(inimg[354][587])[2:].zfill(8)[6])
    print(bin(inimg[354][587])[2:].zfill(8)[7])

    #print(str((binaryArray[300][200]))[0])
    #print(str((binaryArray[300][200]))[1])
    #print(str((binaryArray[300][200]))[2])
    #print(str((binaryArray[300][200]))[3])
    #print(str((binaryArray[300][200]))[4])
    #print(str((binaryArray[300][200]))[5])
    #print(str((binaryArray[300][200]))[6])
    #print(str((binaryArray[390][200]))[7])


    # Assigning the ith element of the binaryArray to the corresponding pixel in each bitPlane (MSB -> LSB)
    for i in range(bitPlaneNumber):
        for j in range(0, inimg.shape[0]):
            for k in range(0, inimg.shape[1]):
                bitPlaneImg[j][k] = bin(inimg[j][k])[2:].zfill(8)[i]

                if (bitPlaneImg[j][k] == 1):
                    bitPlaneImg[j][k] = 255
                else:
                    bitPlaneImg[j][k] = 0

                #print(bin(inimg[j][k])[2:].zfill(8)[i])
                #print(bitPlaneImg[j][k])
        
        bitPlaneImg = bitPlaneImg.astype(int)
        #print(type(bitPlaneImg))

        # Saving the particular bit-plane image to the working directory:
        cv2.imwrite("bitPlane" + str(8-i) + ".jpg",bitPlaneImg)
