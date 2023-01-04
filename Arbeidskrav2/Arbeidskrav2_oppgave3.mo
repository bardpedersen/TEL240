model Arbeidskrav2_oppgave3
  Modelica.Blocks.Continuous.PID pid(Td = 0, Ti = 14.375, k = 0.91225) annotation(
    Placement(visible = true, transformation(origin = {-144, -2}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Math.Feedback feedback annotation(
    Placement(visible = true, transformation(origin = {-202, -2}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Math.Division division annotation(
    Placement(visible = true, transformation(origin = {114, 50}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Continuous.Integrator T(y_start = 25) annotation(
    Placement(visible = true, transformation(origin = {168, 32}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Nonlinear.FixedDelay fixedDelay(delayTime = 3) annotation(
    Placement(visible = true, transformation(origin = {-98, 0}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Math.Gain K(k = 3.5) annotation(
    Placement(visible = true, transformation(origin = {-58, 0}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Sources.Constant Theta_t(k = 23) annotation(
    Placement(visible = true, transformation(origin = {72, 26}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Sources.Step T_env(height = 0, offset = 25, startTime = 0) annotation(
    Placement(visible = true, transformation(origin = {-40, 64}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Sources.Step Set_temp( height = 1,offset = 25, startTime = 20) annotation(
    Placement(visible = true, transformation(origin = {-250, -4}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Math.Add3 add3(k3 = -1)  annotation(
    Placement(visible = true, transformation(origin = {30, 46}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
equation
  connect(pid.y, fixedDelay.u) annotation(
    Line(points = {{-133, -2}, {-110, -2}, {-110, 0}}, color = {0, 0, 127}));
  connect(feedback.y, pid.u) annotation(
    Line(points = {{-193, -2}, {-156, -2}}, color = {0, 0, 127}));
  connect(T.y, feedback.u2) annotation(
    Line(points = {{179, 32}, {192, 32}, {192, -84}, {-202, -84}, {-202, -10}}, color = {0, 0, 127}));
  connect(division.y, T.u) annotation(
    Line(points = {{125, 50}, {140.5, 50}, {140.5, 32}, {156, 32}}, color = {0, 0, 127}));
  connect(fixedDelay.y, K.u) annotation(
    Line(points = {{-87, 0}, {-70, 0}}, color = {0, 0, 127}));
  connect(Theta_t.y, division.u2) annotation(
    Line(points = {{83, 26}, {102, 26}, {102, 44}}, color = {0, 0, 127}));
  connect(Set_temp.y, feedback.u1) annotation(
    Line(points = {{-239, -4}, {-224.5, -4}, {-224.5, -2}, {-210, -2}}, color = {0, 0, 127}));
  connect(K.y, add3.u2) annotation(
    Line(points = {{-46, 0}, {-6, 0}, {-6, 46}, {18, 46}}, color = {0, 0, 127}));
  connect(T_env.y, add3.u1) annotation(
    Line(points = {{-28, 64}, {18, 64}, {18, 54}}, color = {0, 0, 127}));
  connect(add3.y, division.u1) annotation(
    Line(points = {{42, 46}, {80, 46}, {80, 56}, {102, 56}}, color = {0, 0, 127}));
  connect(T.y, add3.u3) annotation(
    Line(points = {{180, 32}, {194, 32}, {194, -44}, {18, -44}, {18, 38}}, color = {0, 0, 127}));
  annotation(
    uses(Modelica(version = "4.0.0")),
    Diagram(coordinateSystem(extent = {{-280, 80}, {200, -100}})),
    Icon(coordinateSystem(extent = {{-300, -200}, {300, 200}})),
    version = "");
end Arbeidskrav2_oppgave3;
