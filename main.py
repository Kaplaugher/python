from litestar import Litestar
from routes import get_items, get_item, create_item, update_item, delete_item

app = Litestar(route_handlers=[get_items, get_item, create_item, update_item, delete_item])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)