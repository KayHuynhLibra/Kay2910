import './App.css';
import React, { useState } from "react";
import Navigation from './components/Navigation';
import ProductListings from './components/ProductListings';
import Products from './data/Products';

const App = () => {
  const [selectedCategory, setSelectedCategory] = useState("all");

  const handleTagClick = (tag) => {
    setSelectedCategory(tag);
  };

  return (
    <div className="flex">
      <Navigation onTagClick={handleTagClick} />
      <ProductListings selectedCategory={selectedCategory} products={Products} />
    </div>
  );
};

export default App;
