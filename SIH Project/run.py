from app import create_app

check = create_app()

if __name__ == "__main__":
    check.run(debug=True)