from litestar import Litestar
from routes import get_opportunities, get_opportunity, create_opportunity, add_files

app = Litestar(route_handlers=[get_opportunities, get_opportunity, create_opportunity, add_files])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)