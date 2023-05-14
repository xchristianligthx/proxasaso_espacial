import cv2

# Leer la imagen
img = cv2.imread("solar-system.jpg")

# Agregar texto a la imagen
cv2.putText(img, "Mercurio", (50, 400), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
cv2.putText(img, "Venus", (300, 400), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
cv2.putText(img, "Tierra", (550, 400), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
cv2.putText(img, "Marte", (800, 400), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
cv2.putText(img, "Júpiter", (1050, 400), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
cv2.putText(img, "Saturno", (1300, 400), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
cv2.putText(img, "Urano", (1550, 400), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
cv2.putText(img, "Neptuno", (1800, 400), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

# Mostrar la imagen
cv2.imshow("Output", img)
cv2.waitKey(0)

# Guardar la imagen con los nombres de los planetas
cv2.imwrite("Solar_systemwithname.jpg", img)
