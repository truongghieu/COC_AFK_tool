import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk,ImageGrab
import customtkinter as ctk
import io

class ImageMarkerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Image Marker Tool")
        self.geometry("800x600")

        # Nút mở ảnh
        self.open_button = ctk.CTkButton(self, text="Open Image", command=self.open_image)
        self.open_button.pack(pady=10)
        
        self.clear_button = ctk.CTkButton(self, text="Clear", command=self.clear_dots)
        self.clear_button.pack(pady=10)

        # Khung canvas để hiển thị ảnh
        self.canvas = tk.Canvas(self, bg="gray", width=800, height=600)
        self.canvas.pack()

        # Nhãn để hiển thị tọa độ pixel
        self.coord_label = ctk.CTkEntry(self, placeholder_text="Marked at: [0, 0]")
        self.coord_label.pack(pady=10)

        # Biến lưu trữ ảnh
        self.img = None
        self.tk_img = None

        # Sự kiện click chuột
        self.canvas.bind("<Button-1>", self.mark_pixel)
        self.bind_all("<Control-v>", self.paste_image)

    def open_image(self):
        # Hộp thoại chọn ảnh
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
        
        if file_path:
            # Mở và hiển thị ảnh
            self.img = Image.open(file_path)
            self.tk_img = ImageTk.PhotoImage(self.img)

            # Thay đổi kích thước canvas theo kích thước ảnh
            # self.canvas.config(width=self.tk_img.width(), height=self.tk_img.height())
            # thay đổi ảnh theo kích thước canvas
            self.tk_img = ImageTk.PhotoImage(self.img.resize((self.canvas.winfo_width(), self.canvas.winfo_height())))
            # Hiển thị ảnh lên canvas
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_img)

    def mark_pixel(self, event):
        # Lấy tọa độ khi người dùng nhấp chuột
        x, y = event.x, event.y

        # Đánh dấu vị trí trên ảnh (vẽ một hình tròn nhỏ tại vị trí click)
        radius = 3
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline="red", width=2)

        # Hiển thị tọa độ lên nhãn
        self.coord_label.delete(0, tk.END)
        self.coord_label.insert(0, f"[{x}, {y}]")

    def paste_image(self, event):
            try:
                # Lấy hình ảnh từ clipboard
                img = ImageGrab.grabclipboard()

                if isinstance(img, Image.Image):
                    # Nếu clipboard chứa một hình ảnh, tải ảnh lên canvas
                    self.load_image(img)
                else:
                    self.coord_label.configure(text="Clipboard does not contain an image")
            except Exception as e:
                self.coord_label.configure(text=f"Error: {str(e)}")
    def load_image(self, img):
        # Cập nhật kích thước canvas dựa trên ảnh
        self.img = img
        self.tk_img = ImageTk.PhotoImage(self.img)
        self.tk_img = ImageTk.PhotoImage(self.img.resize((self.canvas.winfo_width(), self.canvas.winfo_height())))

        # Hiển thị ảnh lên canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_img)
    
    def clear_dots(self):
        # Xóa tọa độ
        self.canvas.delete("all")
# Chạy ứng dụng
if __name__ == "__main__":
    app = ImageMarkerApp()
    app.mainloop()
