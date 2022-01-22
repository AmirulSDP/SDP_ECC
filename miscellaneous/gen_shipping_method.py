my_data=[
('Steel Roofing Deck', 'Steel Flooring System', '', '', '', 'Container'),
('Steel Roofing Deck', 'Steel Flooring System', 'Steel Flooring System, Ternium Losacero 25, 63.5mm (Height)', 'kg', '1.729', 'Container'),
('Steel Roofing Deck', 'Steel Flooring System', 'Steel Flooring System, Ternium Losacero 30, 76.2mm (Height)', 'kg', '1.721', 'Container'),
]


for tup in my_data:
	print(tup+('Bulk Carrier',))
	print(tup+('Container',))
	print(tup+('General Cargo',))


('Steel Roofing Deck', 'Steel Flooring System', '', '', '', 'Container', 'Bulk Carrier',
('Steel Roofing Deck', 'Steel Flooring System', '', '', '', 'Container', 'Container',
('Steel Roofing Deck', 'Steel Flooring System', '', '', '', 'Container', 'General Cargo',
('Steel Roofing Deck', 'Steel Flooring System', 'Steel Flooring System, Ternium Losacero 25, 63.5mm (Height)', 'kg', '1.729', 'Container', 'Bulk Carrier',
('Steel Roofing Deck', 'Steel Flooring System', 'Steel Flooring System, Ternium Losacero 25, 63.5mm (Height)', 'kg', '1.729', 'Container', 'Container',
('Steel Roofing Deck', 'Steel Flooring System', 'Steel Flooring System, Ternium Losacero 25, 63.5mm (Height)', 'kg', '1.729', 'Container', 'General Cargo',
('Steel Roofing Deck', 'Steel Flooring System', 'Steel Flooring System, Ternium Losacero 30, 76.2mm (Height)', 'kg', '1.721', 'Container', 'Bulk Carrier',
('Steel Roofing Deck', 'Steel Flooring System', 'Steel Flooring System, Ternium Losacero 30, 76.2mm (Height)', 'kg', '1.721', 'Container', 'Container',
('Steel Roofing Deck', 'Steel Flooring System', 'Steel Flooring System, Ternium Losacero 30, 76.2mm (Height)', 'kg', '1.721', 'Container', 'General Cargo',
