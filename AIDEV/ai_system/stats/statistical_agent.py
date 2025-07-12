from typing import Any, Dict, List, Union
import numpy as np
from scipy import stats
import pandas as pd
from .base_agent import BaseAgent

class StatisticalAgent(BaseAgent):
    def __init__(self, name: str, config: Dict[str, Any]):
        super().__init__(name, config)
        self.data_cache = {}
        
    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process statistical analysis request"""
        try:
            analysis_type = input_data.get("type")
            data = input_data.get("data", [])
            params = input_data.get("params", {})
            
            if analysis_type == "descriptive":
                return await self.descriptive_stats(data)
            elif analysis_type == "probability":
                return await self.probability_calc(data, params)
            elif analysis_type == "hypothesis":
                return await self.hypothesis_test(data, params)
            elif analysis_type == "correlation":
                return await self.correlation_analysis(data)
            elif analysis_type == "regression":
                return await self.regression_analysis(data, params)
            else:
                return {"error": f"Unknown analysis type: {analysis_type}"}
                
        except Exception as e:
            self.logger.error(f"Error in statistical analysis: {str(e)}")
            return {"error": str(e)}
    
    async def learn(self, data: Dict[str, Any]) -> None:
        """Learn from analysis results"""
        try:
            self.add_to_memory({
                "type": "statistical_result",
                "data": data
            })
            
            # Update data cache if needed
            if "cache_key" in data and "data" in data:
                self.data_cache[data["cache_key"]] = data["data"]
                
        except Exception as e:
            self.logger.error(f"Error in learning: {str(e)}")
    
    async def descriptive_stats(self, data: List[float]) -> Dict[str, Any]:
        """Calculate descriptive statistics"""
        try:
            data_array = np.array(data)
            return {
                "mean": float(np.mean(data_array)),
                "median": float(np.median(data_array)),
                "mode": float(stats.mode(data_array)[0][0]),
                "std": float(np.std(data_array)),
                "variance": float(np.var(data_array)),
                "min": float(np.min(data_array)),
                "max": float(np.max(data_array)),
                "quartiles": {
                    "q1": float(np.percentile(data_array, 25)),
                    "q2": float(np.percentile(data_array, 50)),
                    "q3": float(np.percentile(data_array, 75))
                }
            }
        except Exception as e:
            return {"error": f"Error in descriptive stats: {str(e)}"}
    
    async def probability_calc(self, data: List[float], params: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate probability distributions"""
        try:
            data_array = np.array(data)
            dist_type = params.get("distribution", "normal")
            
            if dist_type == "normal":
                mean, std = np.mean(data_array), np.std(data_array)
                return {
                    "distribution": "normal",
                    "parameters": {
                        "mean": float(mean),
                        "std": float(std)
                    },
                    "pdf": [float(stats.norm.pdf(x, mean, std)) for x in data_array],
                    "cdf": [float(stats.norm.cdf(x, mean, std)) for x in data_array]
                }
            elif dist_type == "exponential":
                scale = 1 / np.mean(data_array)
                return {
                    "distribution": "exponential",
                    "parameters": {"scale": float(scale)},
                    "pdf": [float(stats.expon.pdf(x, scale=scale)) for x in data_array],
                    "cdf": [float(stats.expon.cdf(x, scale=scale)) for x in data_array]
                }
            else:
                return {"error": f"Unsupported distribution: {dist_type}"}
                
        except Exception as e:
            return {"error": f"Error in probability calculation: {str(e)}"}
    
    async def hypothesis_test(self, data: List[float], params: Dict[str, Any]) -> Dict[str, Any]:
        """Perform hypothesis testing"""
        try:
            data_array = np.array(data)
            test_type = params.get("test_type", "t-test")
            alpha = params.get("alpha", 0.05)
            
            if test_type == "t-test":
                t_stat, p_value = stats.ttest_1samp(data_array, params.get("mu", 0))
                return {
                    "test_type": "t-test",
                    "statistic": float(t_stat),
                    "p_value": float(p_value),
                    "significant": p_value < alpha,
                    "alpha": alpha
                }
            elif test_type == "chi-square":
                chi2, p_value = stats.chisquare(data_array)
                return {
                    "test_type": "chi-square",
                    "statistic": float(chi2),
                    "p_value": float(p_value),
                    "significant": p_value < alpha,
                    "alpha": alpha
                }
            else:
                return {"error": f"Unsupported test type: {test_type}"}
                
        except Exception as e:
            return {"error": f"Error in hypothesis testing: {str(e)}"}
    
    async def correlation_analysis(self, data: Dict[str, List[float]]) -> Dict[str, Any]:
        """Calculate correlation between variables"""
        try:
            df = pd.DataFrame(data)
            corr_matrix = df.corr()
            
            return {
                "correlation_matrix": corr_matrix.to_dict(),
                "pearson": corr_matrix.to_dict(),
                "spearman": df.corr(method='spearman').to_dict()
            }
        except Exception as e:
            return {"error": f"Error in correlation analysis: {str(e)}"}
    
    async def regression_analysis(self, data: Dict[str, List[float]], params: Dict[str, Any]) -> Dict[str, Any]:
        """Perform regression analysis"""
        try:
            df = pd.DataFrame(data)
            x_cols = params.get("x_columns", [])
            y_col = params.get("y_column")
            
            if not x_cols or not y_col:
                return {"error": "Missing x_columns or y_column in parameters"}
            
            X = df[x_cols]
            y = df[y_col]
            
            # Simple linear regression
            if len(x_cols) == 1:
                slope, intercept, r_value, p_value, std_err = stats.linregress(X[x_cols[0]], y)
                return {
                    "type": "simple_linear",
                    "coefficients": {
                        "slope": float(slope),
                        "intercept": float(intercept)
                    },
                    "r_squared": float(r_value ** 2),
                    "p_value": float(p_value),
                    "std_error": float(std_err)
                }
            # Multiple linear regression
            else:
                from sklearn.linear_model import LinearRegression
                model = LinearRegression()
                model.fit(X, y)
                
                return {
                    "type": "multiple_linear",
                    "coefficients": dict(zip(x_cols, model.coef_)),
                    "intercept": float(model.intercept_),
                    "r_squared": float(model.score(X, y))
                }
                
        except Exception as e:
            return {"error": f"Error in regression analysis: {str(e)}"}
    
    def get_cached_data(self, key: str) -> Union[Dict[str, Any], None]:
        """Get data from cache"""
        return self.data_cache.get(key)
    
    def clear_cache(self) -> None:
        """Clear data cache"""
        self.data_cache = {}
        self.logger.info("Statistical data cache cleared") 