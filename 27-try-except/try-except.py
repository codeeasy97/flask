#Python Try Except


try:
    f = open('/home/tech/Documents/homespace/project/flask/27-try-except/test_file.txt')
    x = myx
except Exception as e:
    print(e)
else:
    print("else block!")
    print(f.read())
    f.close()
finally:
    print("finally")
