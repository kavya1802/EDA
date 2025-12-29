import React, { useState } from 'react';
import { BarChart, Bar, LineChart, Line, PieChart, Pie, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { TrendingDown, Users, Activity, Package, MapPin, AlertTriangle } from 'lucide-react';

const LinkedInDashboard = () => {
  const [activeTab, setActiveTab] = useState('overview');

  // Sample data
  const churnData = [
    { name: 'Retained', value: 7963, percentage: 79.6 },
    { name: 'Churned', value: 2037, percentage: 20.4 }
  ];

  const geographyData = [
    { country: 'France', churnRate: 16.2, customers: 5014 },
    { country: 'Spain', churnRate: 16.7, customers: 2477 },
    { country: 'Germany', churnRate: 32.4, customers: 2509 }
  ];

  const productData = [
    { products: '1 Product', churnRate: 27.7, customers: 5084 },
    { products: '2 Products', churnRate: 7.6, customers: 4590 },
    { products: '3 Products', churnRate: 16.7, customers: 266 },
    { products: '4 Products', churnRate: 100.0, customers: 60 }
  ];

  const ageData = [
    { age: '18-30', churnRate: 9.5 },
    { age: '31-40', churnRate: 16.8 },
    { age: '41-50', churnRate: 24.9 },
    { age: '51-60', churnRate: 38.4 },
    { age: '60+', churnRate: 56.2 }
  ];

  const activityData = [
    { status: 'Active', churnRate: 14.3, customers: 5151 },
    { status: 'Inactive', churnRate: 26.9, customers: 4849 }
  ];

  const impactMetrics = [
    { metric: 'Customers Saved', value: '400-500', icon: Users },
    { metric: 'Revenue Protected', value: '$800K-1.5M', icon: TrendingDown },
    { metric: 'Churn Reduction', value: '20-25%', icon: Activity },
    { metric: 'ROI Year 1', value: '3.5x-6x', icon: Package }
  ];

  const COLORS = {
    retained: '#10b981',
    churned: '#ef4444',
    primary: '#3b82f6',
    warning: '#f59e0b',
    danger: '#dc2626'
  };

  return (
    <div className="w-full bg-gradient-to-br from-slate-50 to-blue-50 p-8 min-h-screen">
      {/* Header */}
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-8">
          <div className="inline-block bg-blue-600 text-white px-4 py-1 rounded-full text-sm font-semibold mb-4">
            📊 DATA ANALYTICS PROJECT
          </div>
          <h1 className="text-4xl font-bold text-gray-900 mb-3">
            Banking Customer Churn Analysis
          </h1>
          <p className="text-xl text-gray-600 mb-2">
            Identifying Key Drivers of Customer Attrition Through Data Science
          </p>
          <div className="flex items-center justify-center gap-4 text-sm text-gray-500">
            <span>📈 10,000 Customers Analyzed</span>
            <span>•</span>
            <span>🐍 Python | Pandas | Streamlit</span>
            <span>•</span>
            <span>💼 Data Analytics Portfolio Project</span>
          </div>
        </div>

        {/* Key Stats Bar */}
        <div className="grid grid-cols-4 gap-4 mb-8">
          <div className="bg-white rounded-xl shadow-md p-6 text-center border-l-4 border-blue-500">
            <div className="text-3xl font-bold text-gray-900">10,000</div>
            <div className="text-sm text-gray-600 mt-1">Total Customers</div>
          </div>
          <div className="bg-white rounded-xl shadow-md p-6 text-center border-l-4 border-red-500">
            <div className="text-3xl font-bold text-red-600">20.4%</div>
            <div className="text-sm text-gray-600 mt-1">Churn Rate</div>
          </div>
          <div className="bg-white rounded-xl shadow-md p-6 text-center border-l-4 border-green-500">
            <div className="text-3xl font-bold text-green-600">79.6%</div>
            <div className="text-sm text-gray-600 mt-1">Retention Rate</div>
          </div>
          <div className="bg-white rounded-xl shadow-md p-6 text-center border-l-4 border-orange-500">
            <div className="text-3xl font-bold text-orange-600">3</div>
            <div className="text-sm text-gray-600 mt-1">Key Risk Factors</div>
          </div>
        </div>

        {/* Main Content Grid */}
        <div className="grid grid-cols-2 gap-6 mb-6">
          {/* Churn Distribution */}
          <div className="bg-white rounded-xl shadow-lg p-6">
            <h3 className="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
              <TrendingDown className="text-red-500" size={20} />
              Overall Churn Distribution
            </h3>
            <ResponsiveContainer width="100%" height={250}>
              <PieChart>
                <Pie
                  data={churnData}
                  cx="50%"
                  cy="50%"
                  labelLine={false}
                  label={({name, percentage}) => `${name}: ${percentage}%`}
                  outerRadius={80}
                  fill="#8884d8"
                  dataKey="value"
                >
                  <Cell fill={COLORS.retained} />
                  <Cell fill={COLORS.churned} />
                </Pie>
                <Tooltip />
              </PieChart>
            </ResponsiveContainer>
            <div className="mt-4 text-center">
              <p className="text-sm text-gray-600">
                <span className="font-bold text-red-600">2,037 customers</span> churned out of 10,000
              </p>
            </div>
          </div>

          {/* Geography Risk */}
          <div className="bg-white rounded-xl shadow-lg p-6">
            <h3 className="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
              <MapPin className="text-blue-500" size={20} />
              Churn Rate by Geography
            </h3>
            <ResponsiveContainer width="100%" height={250}>
              <BarChart data={geographyData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="country" />
                <YAxis label={{ value: 'Churn Rate (%)', angle: -90, position: 'insideLeft' }} />
                <Tooltip />
                <Bar dataKey="churnRate" fill="#3b82f6">
                  {geographyData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.churnRate > 30 ? COLORS.danger : COLORS.primary} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
            <div className="mt-4 bg-red-50 border-l-4 border-red-500 p-3">
              <p className="text-sm text-red-800 font-semibold">
                ⚠️ Germany shows 32.4% churn - 2x higher than other markets
              </p>
            </div>
          </div>
        </div>

        {/* Key Insights Row */}
        <div className="grid grid-cols-2 gap-6 mb-6">
          {/* Product Holdings */}
          <div className="bg-white rounded-xl shadow-lg p-6">
            <h3 className="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
              <Package className="text-green-500" size={20} />
              Churn by Product Holdings
            </h3>
            <ResponsiveContainer width="100%" height={250}>
              <BarChart data={productData.slice(0, 3)}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="products" />
                <YAxis label={{ value: 'Churn Rate (%)', angle: -90, position: 'insideLeft' }} />
                <Tooltip />
                <Bar dataKey="churnRate" fill="#10b981">
                  {productData.slice(0, 3).map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.churnRate > 20 ? COLORS.danger : COLORS.retained} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
            <div className="mt-4 bg-green-50 border-l-4 border-green-500 p-3">
              <p className="text-sm text-green-800 font-semibold">
                ✓ 2 products = 72% lower churn rate (7.6% vs 27.7%)
              </p>
            </div>
          </div>

          {/* Age Impact */}
          <div className="bg-white rounded-xl shadow-lg p-6">
            <h3 className="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
              <Activity className="text-purple-500" size={20} />
              Churn Rate by Age Group
            </h3>
            <ResponsiveContainer width="100%" height={250}>
              <LineChart data={ageData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="age" />
                <YAxis label={{ value: 'Churn Rate (%)', angle: -90, position: 'insideLeft' }} />
                <Tooltip />
                <Line type="monotone" dataKey="churnRate" stroke="#ef4444" strokeWidth={3} dot={{ r: 6 }} />
              </LineChart>
            </ResponsiveContainer>
            <div className="mt-4 bg-orange-50 border-l-4 border-orange-500 p-3">
              <p className="text-sm text-orange-800 font-semibold">
                📈 Churn increases with age: 60+ customers show 56.2% churn
              </p>
            </div>
          </div>
        </div>

        {/* Top 3 Findings Banner */}
        <div className="bg-gradient-to-r from-blue-600 to-blue-800 rounded-xl shadow-xl p-8 mb-6 text-white">
          <h2 className="text-2xl font-bold mb-6 text-center">🎯 Top 3 Critical Findings</h2>
          <div className="grid grid-cols-3 gap-6">
            <div className="text-center">
              <div className="text-5xl font-bold mb-2">32.4%</div>
              <div className="text-blue-100 font-semibold mb-1">Germany Churn Rate</div>
              <div className="text-sm text-blue-200">2x higher than France/Spain</div>
            </div>
            <div className="text-center border-x border-blue-400 px-4">
              <div className="text-5xl font-bold mb-2">72%</div>
              <div className="text-blue-100 font-semibold mb-1">Risk Reduction</div>
              <div className="text-sm text-blue-200">With 2+ products vs single</div>
            </div>
            <div className="text-center">
              <div className="text-5xl font-bold mb-2">88%</div>
              <div className="text-blue-100 font-semibold mb-1">Higher Risk</div>
              <div className="text-sm text-blue-200">For inactive members</div>
            </div>
          </div>
        </div>

        {/* Business Impact */}
        <div className="bg-white rounded-xl shadow-lg p-8 mb-6">
          <h2 className="text-2xl font-bold text-gray-900 mb-6 text-center">💼 Projected Business Impact</h2>
          <div className="grid grid-cols-4 gap-4">
            {impactMetrics.map((item, index) => {
              const Icon = item.icon;
              return (
                <div key={index} className="text-center p-4 bg-gradient-to-br from-blue-50 to-indigo-50 rounded-lg border border-blue-200">
                  <Icon className="mx-auto text-blue-600 mb-2" size={32} />
                  <div className="text-2xl font-bold text-gray-900">{item.value}</div>
                  <div className="text-sm text-gray-600 mt-1">{item.metric}</div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Strategic Recommendations */}
        <div className="bg-white rounded-xl shadow-lg p-8 mb-6">
          <h2 className="text-2xl font-bold text-gray-900 mb-6 text-center">📌 Strategic Recommendations</h2>
          <div className="grid grid-cols-3 gap-6">
            <div className="border-l-4 border-green-500 pl-4">
              <h3 className="font-bold text-gray-900 mb-2">1. Multi-Product Cross-Sell</h3>
              <p className="text-sm text-gray-600 mb-2">
                Target 5,100 single-product customers with bundled offerings
              </p>
              <p className="text-xs text-green-700 font-semibold">
                ✓ Expected: 850-1,000 saves annually
              </p>
            </div>
            <div className="border-l-4 border-blue-500 pl-4">
              <h3 className="font-bold text-gray-900 mb-2">2. Re-Engagement Campaign</h3>
              <p className="text-sm text-gray-600 mb-2">
                Activate 4,800 inactive members through incentives
              </p>
              <p className="text-xs text-blue-700 font-semibold">
                ✓ Expected: 400-500 saves annually
              </p>
            </div>
            <div className="border-l-4 border-orange-500 pl-4">
              <h3 className="font-bold text-gray-900 mb-2">3. Germany-Specific Strategy</h3>
              <p className="text-sm text-gray-600 mb-2">
                Address 32% churn with targeted interventions
              </p>
              <p className="text-xs text-orange-700 font-semibold">
                ✓ Expected: 400-500 German saves
              </p>
            </div>
          </div>
        </div>

        {/* Technical Skills Badge */}
        <div className="bg-gradient-to-r from-slate-800 to-slate-900 rounded-xl shadow-lg p-6 text-white">
          <div className="text-center">
            <h3 className="text-lg font-bold mb-4">🛠️ Technical Skills Demonstrated</h3>
            <div className="flex flex-wrap justify-center gap-3">
              {['Python', 'Pandas', 'NumPy', 'Matplotlib', 'Seaborn', 'Plotly', 'Streamlit', 'EDA', 'Data Cleaning', 'Statistical Analysis', 'Data Visualization', 'Business Intelligence'].map((skill, i) => (
                <span key={i} className="bg-slate-700 px-4 py-2 rounded-full text-sm font-semibold">
                  {skill}
                </span>
              ))}
            </div>
          </div>
        </div>

        {/* Footer CTA */}
        <div className="mt-8 text-center">
          <div className="inline-block bg-white rounded-lg shadow-md p-6">
            <p className="text-gray-600 mb-3">
              💡 <span className="font-semibold">Want to learn more about this analysis?</span>
            </p>
            <p className="text-sm text-gray-500">
              Full code, interactive dashboard, and detailed insights available on request
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LinkedInDashboard;