#Uses match case to tell your dumbass exactly what the extension is

def main():
  file=input("Enter the file name: ")
  ext=file.lower().strip().split(".")[-1]
  f_type(ext.lower())

def f_type(ext):
  match ext:
    case "gif":
      print("image/gif")
    case "jpg":
      print("image/jpeg")
    case "jpeg":
      print("image/jpeg")
    case "png":
      print("image/png")
    case "pdf":
      print("application/pdf")
    case "txt":
      print("text/plain")
    case "zip":
      print("application/zip")
    case _:
      print("application/octet-stream")

main()
