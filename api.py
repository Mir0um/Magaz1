from flask import Flask, request, jsonify
from inventory import InventoryManager
from reporting import ReportGenerator

app = Flask(__name__)

inventory_manager = InventoryManager()
report_generator = ReportGenerator()

@app.route('/check_item_availability', methods=['POST'])
def check_item_availability():
    data = request.get_json()
    item_id = data.get('item_id')
    quantity = data.get('quantity')
    
    if item_id and quantity is not None:
        available = inventory_manager.is_item_available(item_id, quantity)
        return jsonify({'available': available})
    
    return jsonify({'error': 'Invalid data'}), 400

@app.route('/purchase_item', methods=['POST'])
def purchase_item():
    data = request.get_json()
    item_id = data.get('item_id')
    quantity = data.get('quantity')
    
    if item_id and quantity is not None:
        success = inventory_manager.purchase_item(item_id, quantity)
        return jsonify({'success': success})
    
    return jsonify({'error': 'Invalid data'}), 400

@app.route('/process_purchases', methods=['POST'])
def process_purchases():
    data = request.get_json()
    purchase_list = data.get('purchase_list')
    
    if purchase_list:
        inventory_manager.process_multiple_purchases(purchase_list)
        return jsonify({'success': True})
    
    return jsonify({'error': 'Invalid data'}), 400

@app.route('/generate_report', methods=['GET'])
def generate_report():
    inventory_report = report_generator.generate_inventory_report(inventory_manager.inventory)
    return jsonify({'report': inventory_report})

if __name__ == '__main__':
    app.run(debug=True)
