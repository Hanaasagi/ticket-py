#![feature(specialization)]

#[macro_use]
extern crate pyo3;
extern crate ticket;

use pyo3::prelude::*;
use std::cell::RefCell;
use std::ptr;

#[pyclass]
struct Ticketing {
    ticketing: RefCell<ticket::Ticketing>
}


impl Ticketing {
    fn new() -> Self {
        Self {
            ticketing: RefCell::new(ticket::Ticketing::new())
        }
    }
}


#[pymethods]
impl Ticketing {
    #[new]
    fn __new__(obj: &PyRawObject) -> PyResult<()> {
        obj.init(|_| Self::new())
    }

    fn gen(&self) -> Vec<u8> {
        self.ticketing.borrow_mut().gen().as_bytes().to_vec()
    }
}


#[pyfunction]
fn encode(id: Vec<u8>) -> String {
    let mut arr: [u8; 12] = [0u8; 12];
    copy_memory(&id, &mut arr);
    ticket::encode(ticket::ID::new(arr))
}


#[pyfunction]
fn decode(id: String) -> Vec<u8> {
    ticket::decode(&id).as_bytes().to_vec()
}


fn copy_memory(src: &[u8], dst: &mut [u8]) {
    let len_src = src.len();
    assert!(dst.len() >= len_src);
    unsafe {
        ptr::copy_nonoverlapping(src.as_ptr(), dst.as_mut_ptr(), len_src);
    }
}


#[pymodinit]
fn ticket(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Ticketing>()?;
    m.add_function(wrap_function!(encode))?;
    m.add_function(wrap_function!(decode))?;
    Ok(())
}
