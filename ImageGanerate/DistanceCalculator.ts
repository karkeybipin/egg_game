import { useState } from "react";

function DistanceCalculator() {
  const [point1, setPoint1] = useState({ x1: "", y1: "" });
  const [point2, setPoint2] = useState({ x2: "", y2: "" });
  const [distance, setDistance] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    if (name.includes("1")) {
      setPoint1({ ...point1, [name]: value });
    } else {
      setPoint2({ ...point2, [name]: value });
    }
  };

  const calculateDistance = (e) => {
    e.preventDefault();
    const x1 = parseFloat(point1.x1);
    const y1 = parseFloat(point1.y1);
    const x2 = parseFloat(point2.x2);
    const y2 = parseFloat(point2.y2);

    const dx = x2 - x1;
    const dy = y2 - y1;
    const dist = Math.sqrt(dx * dx + dy * dy);
    setDistance(dist.toFixed(2));
  };

  return (
    <div style={{ padding: "20px", textAlign: "center" }}>
      <h2>2D Distance Calculator</h2>
      <form onSubmit={calculateDistance}>
        <div>
          <label>
            Point 1 (x1, y1):
            <input
              type="number"
              name="x1"
              value={point1.x1}
              onChange={handleChange}
              placeholder="x1"
              required
            />
            <input
              type="number"
              name="y1"
              value={point1.y1}
              onChange={handleChange}
              placeholder="y1"
              required
            />
          </label>
        </div>
        <div style={{ marginTop: "10px" }}>
          <label>
            Point 2 (x2, y2):
            <input
              type="number"
              name="x2"
              value={point2.x2}
              onChange={handleChange}
              placeholder="x2"
              required
            />
            <input
              type="number"
              name="y2"
              value={point2.y2}
              onChange={handleChange}
              placeholder="y2"
              required
            />
          </label>
        </div>
        <button type="submit" style={{ marginTop: "10px" }}>
          Calculate Distance
        </button>
      </form>

      {distance && (
        <div style={{ marginTop: "20px" }}>
          <h3>The distance between the points is: {distance}</h3>
        </div>
      )}
    </div>
  );
}

export default DistanceCalculator;
