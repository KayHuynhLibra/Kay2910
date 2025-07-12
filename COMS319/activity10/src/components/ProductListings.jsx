const ProductListings = ({ selectedCategory, products }) => {
    const filtered = selectedCategory === 'all' ? products : products.filter(product => product.category === selectedCategory);
  
    return (
      <div className="ml-[300px] bg-yellow-100 min-h-screen p-6">
        <h1 className="text-4xl font-extrabold text-black text-center mb-6">Products ({filtered.length})</h1>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          {filtered.map(product => (
            <div key={product.id} className="bg-white rounded-lg shadow-md p-4">
              <img src={product.image} alt={product.title} className="w-full h-48 object-contain"/>
              <div className="mt-4 flex justify-between items-center">
                <h3 className="text-lg font-semibold text-gray-700">{product.title}</h3>
                <h3 className="text-green-700 font-extrabold text-lg">${product.price}</h3>
              </div>
              <div className="mt-2 text-gray-600">{product.description}</div>
              <div className="mt-2 text-sm text-amber-700 font-semibold">{product.category}</div>
              <div className="mt-1 text-black text-lg">Rating: {product.rating.rate}</div>
            </div>
          ))}
        </div>
      </div>
    );
  };
  
  export default ProductListings;
  