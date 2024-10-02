from litestar import get, post
from typing import List
from models import Opportunity, File
import database as database
from datetime import date

@get("/opportunities")
async def get_opportunities() -> List[Opportunity]:
    return database.opportunities

@get("/opportunity/{opportunity_id:int}")
async def get_opportunity(opportunity_id: int) -> Opportunity:
    opportunity = next((opp for opp in database.opportunities if opp.id == opportunity_id), None)
    if opportunity is None:
        raise ValueError("Opportunity not found")
    return opportunity

@post("/opportunities")
async def create_opportunity(opportunity: Opportunity) -> Opportunity:
    opportunity.id = len(database.opportunities) + 1
    opportunity.date = date.today()  # Set the date to today if not provided
    database.opportunities.append(opportunity)
    return opportunity

@post("/opportunity/{opportunity_id:int}/files")
async def add_files(opportunity_id: int, files: List[File]) -> Opportunity:
    opportunity = next((opp for opp in database.opportunities if opp.id == opportunity_id), None)
    if opportunity is None:
        raise ValueError("Opportunity not found")
    opportunity.files.extend(files)
    return opportunity