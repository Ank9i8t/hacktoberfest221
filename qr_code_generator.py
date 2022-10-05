# Import module   
#pip install wifi-qrcode-generator
import wifi_qrcode_generator as qr


print(" Enter your SSID for the WIFI QR-CODE:")
ssid_var = input()

print("Enter your Wifi Password for the WIFI QR-CODE:")
pw_var = input()

print("Generate QR Code with SSID: %s and PW: %s " %(str(ssid_var),str(pw_var)))
print("See in the Folder for your QR Code")

# Use wifi_qrcode() to create a QR image
qr_pic = qr.wifi_qrcode(str(ssid_var), False, 'WPA', str(pw_var))


# Display the  QR image
qr_pic.show()

# Save the image as PNG file
qr_pic.save("WIFI_QR.png")