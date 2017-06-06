# sql 删除语句

## 基本
   DELETE FROM table_name
   WHERE some_column=some_value;
 注:当 WHERE 字句为空时，删除全表 
  
  UPDATE table_name
   SET column1=value1,column2=value2,...
    WHERE some_column=some_value;

  SELECT DISTINCT column_name,column_name
   FROM table_name;

  SELECT column_name,column_name
   FROM table_name;

  INSERT INTO table_name
   VALUES (value1,value2,value3,...);





## WHERE 字句: --- 用于过滤记录
    WHERE 字句用于提取满足指定标准的记录
    WHERE + 条件(筛选行)
       条件：列，比较运算符，值
       比较运算符 =,<,>,>=,<=,!=,<>
    e.g.  Select * from emp where enmap=""

select 选择字段 from 表名 WHERE 条件

delete from 表名 WHERE  条件
update 表名 SET 更新字典 WHERE 条件 
    
