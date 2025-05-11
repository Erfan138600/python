import tkinter as tk

# تابعی برای انجام عملیات کم و اضافه کردن
def calculate():
    try:
        num = int(entry.get())  # گرفتن عدد از ورودی
        increment = int(spinbox.get())  # گرفتن مقداری که باید کم یا اضافه بشه
        result = num + increment  # انجام عملیات جمع یا تفریق
        result_label.config(text=f"نتیجه: {result}")  # نمایش نتیجه
    except ValueError:
        result_label.config(text="لطفاً یک عدد معتبر وارد کنید")  # اگر ورودی معتبر نبود

# راه‌اندازی پنجره اصلی
root = tk.Tk()
root.title("محاسبه کم یا اضافه کردن")

# اضافه کردن یک برچسب برای توضیحات
label = tk.Label(root, text="عدد را وارد کنید:")
label.pack(pady=10)

# ورودی عددی برای گرفتن مقدار
entry = tk.Entry(root)
entry.pack(pady=5)

# توضیح برای انتخاب مقدار برای کم یا اضافه کردن
spinbox_label = tk.Label(root, text="مقدار کم یا اضافه کنید:")
spinbox_label.pack(pady=5)

# ایجاد یک Spinbox برای انتخاب عدد کم یا اضافه
spinbox = tk.Spinbox(root, from_=-10, to=10)  # از -10 تا 10
spinbox.pack(pady=5)

# دکمه برای انجام محاسبه
calculate_button = tk.Button(root, text="محاسبه", command=calculate)
calculate_button.pack(pady=10)

# برچسب برای نمایش نتیجه
result_label = tk.Label(root, text="نتیجه:")
result_label.pack(pady=20)

# راه‌اندازی رابط گرافیکی
root.mainloop()
