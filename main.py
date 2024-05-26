from fastapi import FastAPI
from controllers.magic_item_controller import router

app = FastAPI()
app.include_router(router, prefix="/items")


def main():


if __name__ == '__main__':
    main()
