from flask import Flask, request
from typing import List, Optional

app = Flask(__name__)

approved_protocols = ['2G', '3G', '4G']
error_str = ' or '.join(approved_protocols)
@app.route('/search/', methods=['GET'],)
def search():
    cell_tower_ids: List[int] = request.args.getlist("cell_tower_id", type=int)

    if not cell_tower_ids:
        return "You must specify at least 1 cell_tower_id", 400
    elif 0 in cell_tower_ids:
        return "cell_tower_id must be bigger than zero", 400
    
    phone_prefixes: List[int] = request.args.getlist("phone_prefix")
    for phone in phone_prefixes:
        star = phone.find("*")
        if not phone[:star].isdigit():
            return f"phone_prefixes must be digits\nerror in {phone}", 400
        if len(phone[:star]) > 10:
            return f"Length of phone_prefix must be less or equal to 10\nerror in {phone}", 400
        if not phone.endswith('*'):
            return f"phone_prefixes must ends with *\nerror in {phone}", 400


    protocols: List[str] = request.args.getlist("protocol")
    for protocol in protocols:
        if protocol not in protocols:
            return f'Protocols formtats: {error_str}', 400


    signal_level: Optional[float] = request.args.get(
        "signal_level", type = float, default = None
    )
    # date_from: List[int]

    return(
        f"Search for {cell_tower_ids} cell towers. Search criteria: "
        f"phone_prefixes = {phone_prefixes},"
        f"protocol = {protocols},"
        f"signal_level = {signal_level}"
    )

if __name__ == "__main__":
    app.run(debug=True)