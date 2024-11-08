import streamlit as st
import pandas as pd

def main():
    st.title('CSV 파일 업로더')
    
    # 파일 업로더 위젯 생성
    uploaded_file = st.file_uploader("CSV 파일을 선택하세요", type=['csv'])
    
    if uploaded_file is not None:
        try:
            # CSV 파일을 데이터프레임으로 읽기
            df = pd.read_csv(uploaded_file)
            
            # 기본 정보 표시
            st.write("### 데이터 미리보기")
            st.write(df.head())
            
            st.write("### 데이터 정보")
            st.write(f"행 수: {df.shape[0]}")
            st.write(f"열 수: {df.shape[1]}")
            
            # 컬럼 정보 표시
            st.write("### 컬럼 목록")
            st.write(df.columns.tolist())
            
        except Exception as e:
            st.error(f"파일을 읽는 중 오류가 발생했습니다: {e}")

if __name__ == '__main__':
    main()
